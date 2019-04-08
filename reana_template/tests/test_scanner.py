# Copyright (C) 2019 New York University.
#
# This file is part of REANA Templates. REANA Templates is free software; you
# can redistribute it and/or modify it under the terms of the MIT License; see
# LICENSE file for more details.

"""Test basic token scanner functionality to collect template parameter values
from standard input.
"""

from unittest import TestCase

from reana_template.scanner import Scanner, ListReader


class TestScanne(TestCase):
    def test_scan_scalar_values(self):
        """Test parsing of scalar tokens."""
        sc = Scanner(reader=ListReader(['3', '34.56', 'FALSE', 'data/names.txt', 'Some text']))
        self.assertEqual(sc.next_int(), 3)
        self.assertEqual(sc.next_float(), 34.56)
        self.assertFalse(sc.next_bool())
        self.assertEqual(sc.next_file(), 'data/names.txt')
        self.assertEqual(sc.next_string(), 'Some text')
        # Value errors when parsing invalid tokens
        sc = Scanner(reader=ListReader(['3', 'FALSE', 'data/names.txt']))
        with self.assertRaises(ValueError):
            sc.next_bool()
        with self.assertRaises(ValueError):
            sc.next_int()
        with self.assertRaises(ValueError):
            sc.next_float()
