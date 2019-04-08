# Copyright (C) 2019 New York University.
#
# This file is part of REANA Templates. REANA Templates is free software; you
# can redistribute it and/or modify it under the terms of the MIT License; see
# LICENSE file for more details.

"""Test loading REANA templates from file."""

import os
import unittest

from unittest import TestCase

from reana_template import REANATemplate
from reana_template.util import load_template

import reana_template.parameter.declaration as pd


class TestLoadTemplate(TestCase):
    def test_load_file(self):
        """Test loading files in either Yaml or Json format from disk using the
        load_template method.
        """
        # Load a Yaml file
        obj = load_template(os.path.abspath('reana_template/tests/files/reana.yaml'))
        self.assertEqual(obj['version'], '0.3.0')
        # Load a Json file
        obj = load_template(os.path.abspath('reana_template/tests/files/schema.json'))
        self.assertEqual(obj['type'], 'object')

    def test_load_template_with_parameters(self):
        """Test loading a REANA workflow template that does contain template
        parameter declarations.
        """
        template = REANATemplate.load('reana_template/tests/files/template.yaml')
        self.assertTrue(isinstance(template.workflow_spec, dict))
        self.assertEqual(len(template.parameters), 2)
        # Code file parameter
        p_code = template.get_parameter('codeFile')
        self.assertEqual(p_code.name, 'Code File')
        self.assertEqual(p_code.data_type, pd.DT_FILE)
        # Sleep time parameter
        p_sleep = template.get_parameter('sleeptime')
        self.assertEqual(p_sleep.name, 'sleeptime')
        self.assertEqual(p_sleep.data_type, pd.DT_INTEGER)

    def test_load_simple_template(self):
        """Test loading a simple REANA workflow template that does not contain
        any template parameter.
        """
        template = REANATemplate.load('reana_template/tests/files/simple-template.yaml')
        self.assertTrue(isinstance(template.workflow_spec, dict))
        self.assertEqual(len(template.parameters), 0)
