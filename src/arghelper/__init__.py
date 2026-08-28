# Copyright (c) 2014-2016 The arghelper developers. All rights reserved.
# Project site: https://github.com/questrail/arghelper
# Use of this source code is governed by a MIT-style license that
# can be found in the LICENSE.txt file for the project.
"""Provide helper functions for argparse"""

# Standard module imports
import argparse
import os

__version__ = "0.6.0"


def extant_file(arg):
    """Facade for extant_item(arg, arg_type="file")"""
    return extant_item(arg, "file")


def extant_dir(arg):
    """Facade for extant_item(arg, arg_type="directory")"""
    return extant_item(arg, "directory")


def extant_item(arg, arg_type):
    """Determine if parser argument is an existing file or directory.

    This technique comes from http://stackoverflow.com/a/11541450/95592
    and from http://stackoverflow.com/a/11541495/95592

    Args:
        arg: parser argument containing filename to be checked
        arg_type: string of either "file" or "directory"

    Returns:
        If the item exists, return the filename or directory name.

    Raises:
        argparse.ArgumentTypeError: If the file or directory does not exist.
            argparse catches this from a ``type=`` callable and reports it as
            a usage error naming the offending argument.
        ValueError: If arg_type is neither "file" nor "directory".
    """
    if arg_type == "file":
        if not os.path.isfile(arg):
            raise argparse.ArgumentTypeError(f"The file {arg} does not exist.")
        # File exists so return the filename
        return arg
    elif arg_type == "directory":
        if not os.path.isdir(arg):
            raise argparse.ArgumentTypeError(f"The directory {arg} does not exist.")
        # Directory exists so return the directory name
        return arg
    else:
        raise ValueError(
            f'arg_type must be either "file" or "directory", not {arg_type!r}.'
        )


def parse_config_input_output(args=None):
    """Parse the args using the config_file, input_dir, output_dir pattern

    Args:
        args: Command line arguments *including* the program name, such as
            sys.argv. If None, sys.argv is read when the function is called.

    Returns:
        The populated namespace object from parser.parse_args().

    Raises:
        SystemExit: If the arguments are missing or do not exist on disk,
            argparse prints a usage message and exits with status 2.
    """
    parser = argparse.ArgumentParser(
        description="Process the input files using the given config"
    )
    parser.add_argument(
        "config_file", help="Configuration file.", metavar="FILE", type=extant_file
    )
    parser.add_argument(
        "input_dir",
        help="Directory containing the input files.",
        metavar="DIR",
        type=extant_dir,
    )
    parser.add_argument(
        "output_dir",
        help="Directory where the output files should be saved.",
        metavar="DIR",
        type=extant_dir,
    )
    return parser.parse_args(None if args is None else args[1:])


def parse_config(args=None):
    """Parse the args using the config_file pattern

    Args:
        args: Command line arguments *including* the program name, such as
            sys.argv. If None, sys.argv is read when the function is called.

    Returns:
        The populated namespace object from parser.parse_args().

    Raises:
        SystemExit: If the arguments are missing or do not exist on disk,
            argparse prints a usage message and exits with status 2.
    """
    parser = argparse.ArgumentParser(description="Read in the config file")
    parser.add_argument(
        "config_file", help="Configuration file.", metavar="FILE", type=extant_file
    )
    return parser.parse_args(None if args is None else args[1:])
