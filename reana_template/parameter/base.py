# Copyright (C) 2019 New York University.
#
# This file is part of REANA Templates. REANA Templates is free software; you
# can redistribute it and/or modify it under the terms of the MIT License; see
# LICENSE file for more details.

"""Base class definitions to work with template parameters."""

import reana_template.parameter.declaration as pd


class TemplateParameter(object):
    """The template parameter class is a simple wrapper around a dictionary that
    contains a parameter declaration. The wrapper provides easy access to the
    diccerent components of the parameter declaration.
    """
    def __init__(self, obj, children=None):
        """Initialize the different attributes of a template parameter
        declaration from the given dictionary.

        Parameters
        ----------
        obj: dict
            Dictionary containing the template parameter declaration properties
        children: list(reana_template.parameter.TemplateParameter), optional
            Optional list of parameter children for parameter lists or records
        """
        self.obj = obj
        self.identifier = obj[pd.LABEL_ID]
        self.name = obj[pd.LABEL_NAME]
        self.data_type = obj[pd.LABEL_DATATYPE]
        self.description = obj[pd.LABEL_DESCRIPTION]
        self.index = obj[pd.LABEL_INDEX]
        self.default_value = obj[pd.LABEL_DEFAULT] if pd.LABEL_DEFAULT in obj else None
        self.is_required = obj[pd.LABEL_REQUIRED]
        self.values = obj[pd.LABEL_VALUES] if pd.LABEL_VALUES in obj else None
        self.children = children

    def add_child(self, para):
        """Short-cut to add an element to the list of child parameter.

        Parameters
        ----------
        para: reana_template.parameter.TemplateParameter
            Template parameter instance for child parameter
        """
        self.children.append(para)

    def has_children(self):
        """Test if a parameter has children. Only returns True if the list of
        children is not None and not empty.

        Returns
        -------
        bool
        """
        if not self.children is None:
            return len(self.children) > 0
        return False
        
    def to_dict(self):
        """Added for clarity. This method simply returns the wrapped parameter
        declaration dictionary.

        Returns
        -------
        dict
        """
        return self.obj
