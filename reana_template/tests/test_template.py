# Copyright (C) 2019 New York University.
#
# This file is part of REANA Templates. REANA Templates is free software; you
# can redistribute it and/or modify it under the terms of the MIT License; see
# LICENSE file for more details.

"""Test REANATemplate functionality."""


from unittest import TestCase

from reana_template import REANATemplate

import reana_template.parameter.declaration as pd


class TestREANATemplate(TestCase):
    def test_sort(self):
        """Test the sort functionality of the template list_parameters method.
        """
        # Create a new REANATemplate with an empty workflow specification and
        # a list of five parameters
        template = REANATemplate(
            workflow_spec={},
            parameters=[
                pd.parameter_declaration('A', index=1),
                pd.parameter_declaration('B'),
                pd.parameter_declaration('C'),
                pd.parameter_declaration('D', index=2),
                pd.parameter_declaration('E', index=1)
            ],
            validate=True
        )
        # Get list of sorted parameter identifier from listing
        keys = [p[pd.LABEL_ID] for p in template.list_parameter()]
        self.assertEqual(keys, ['B', 'C', 'A', 'E', 'D'])
