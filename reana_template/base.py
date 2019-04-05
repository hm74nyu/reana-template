# Copyright (C) 2019 New York University.
#
# This file is part of REANA Templates. REANA Templates is free software; you
# can redistribute it and/or modify it under the terms of the MIT License; see
# LICENSE file for more details.

"""REANA Template class. A REANA template has two main components: (1) a REANA
workflow declaration and (2) a list of optional template parameters.

The workflow declaration may contain references to template parameters. The
template parameters are for example used to render front-end forms for parameter
input. Given an association of parameter identifier with values we use this to
create a valid REANA workflow specification by replacing the references to
template  parameters with the respective values in the value dictionary.
"""

from reana_template.util import load_template

import reana_template.parameter.declaration as pd


"""Labels for top-level elements in REANA Templates."""
LABEL_PARAMETERS = 'parameters'
LABEL_WORKFLOW = 'workflow'


class REANATemplate(object):
    """A REANA workflow template contains a REANA workflow specification and
    a dictionary of template parameter declarations. Parameter declarations are
    keyed by heir unique identifier in the dictionary.
    """
    def __init__(self, workflow_spec, parameters=None, validate=False):
        """Initialize the workflow specification and the list of template
        parameter declaration. Template parameters are optional.

        If the valid flag is True all given template parameter declarations are
        validated against the parameter schema. Raises ValueError if any of
        the given parameter declarations fails the validation.

        Raises ValueError if the identifier for the given parameter declarations
        are not unique.

        Parameters
        ----------
        workflow_spec: dict
            Json object containing a REANA workflow specification
        parameters: list, optional
            List of workflow template parameter declarations
        validate: bool, optional
            Flag indicating if given template parameter declarations are to be
            validated against the parameter schema or not.
        """
        self.workflow_spec = workflow_spec
        # Add given parameter declaration to the parameters list. Ensure that
        # all default values are set
        self.parameters = dict()
        if not parameters is None:
            for para in parameters:
                # Validate the template parameters if the validate flag is True
                if validate:
                    pd.validate_parameter(para)
                self.parameters[para[pd.LABEL_ID]] = pd.set_defaults(para)

    def get_parameter(self, identifier):
        """Short-cut to access the declaration for a parameter with the given
        identifier.

        Parameters
        ----------
        identifier: string
            Unique parameter declaration identifier

        Returns
        -------
        dict
        """
        return self.parameters.get(identifier)

    def list_parameter(self):
        """Get a sorted list of parameter declarations. Elements are sorted by
        their index value. Ties are broken using the unique parameter
        identifier.

        Returns
        -------
        list
        """
        params = self.parameters.values()
        return sorted(params, key=lambda p: (p[pd.LABEL_INDEX], p[pd.LABEL_ID]))

    @staticmethod
    def load(filename, validate=True):
        """Load REANA workflow template declaration from file and return an
        instance of the REANATemplate class.

        Raises ValueError if the file does not contain a valid workflow
        template.

        Parameters
        ----------
        filename: string
            Path to file containing the REANA workflow template declaration
        validate: bool, optional
            Flag indicating whether parameter declarations in the template
            should be validated or not

        Returns
        -------
        reana_template.base.REANATemplate
        """
        # Load Json object from given file
        obj = load_template(filename)
        # Ensure that the Json object contains at least the 'workflow' element
        # and at most 'workflow' and 'parameter' elements
        if not LABEL_WORKFLOW in obj:
            raise ValueError('missing element \'workflow\'')
        for key in obj:
            if not key in [LABEL_WORKFLOW, LABEL_PARAMETERS]:
                raise ValueError('invalid element \'' + str(key) + '\'')
        # Return new REANA Template object
        return REANATemplate(
            obj.get(LABEL_WORKFLOW),
            parameters=obj.get(LABEL_PARAMETERS),
            validate=validate
        )
