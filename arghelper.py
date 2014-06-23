#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 The arghelper developers. All rights reserved.
# Project site: https://github.com/matthewrankin/arghelper
# Use of this source code is governed by a MIT-style license that
# can be found in the LICENSE.txt file for the project.
"""Provide helper functions for argparse

"""

# Try to future proof code so that it's Python 3.x ready
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

# Standard module imports
import argparse
import os

# The version as used in the setup.py
__version__ = '0.1'


def extant_file(arg):
    """Facade for extant_item(arg, arg_type="file")
    """
    return extant_item(arg, "file")


def extant_dir(arg):
    """Facade for extant_item(arg, arg_type="directory")
    """
    return extant_item(arg, "directory")


def extant_item(arg, arg_type):
    """Determine if parser argument is an existing file or directory.

    This technique comes from http://stackoverflow.com/a/11541450/95592
    and from http://stackoverflow.com/a/11541495/95592

    Args:
        arg: parser argument containing filename to be checked
        arg_type: string of either "file" or "directory"

    Returns:
        If the file exists, return the filename or directory.

    Raises:
        If the file does not exist, raise a parser error.
    """
    if arg_type == "file":
        if not os.path.isfile(arg):
            raise argparse.ArgumentError(
                None,
                "The file {arg} does not exist.".format(arg=arg))
        else:
            # File exists so return the filename
            return arg
    elif arg_type == "directory":
        if not os.path.isdir(arg):
            raise argparse.ArgumentError(
                None,
                "The directory {arg} does not exist.".format(arg=arg))
        else:
            # Directory exists so return the directory name
            return arg