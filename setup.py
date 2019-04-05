# Copyright (C) 2019 New York University.
#
# This file is part of REANA Templates. REANA Templates is free software; you
# can redistribute it and/or modify it under the terms of the MIT License; see
# LICENSE file for more details.

from setuptools import setup


install_requires=[
	'jsonschema',
    'pyyaml>=5.1'
]


tests_require = [
    'nose'
]


setup(
    name='reana-template',
    version='0.1.0',
    description='Templates for REANA workflows',
    license='MIT',
    packages=['reana_template'],
    test_suite='nose.collector',
    tests_require=tests_require,
    install_requires=install_requires
)