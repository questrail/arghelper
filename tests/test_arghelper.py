# Copyright (c) 2014-2016 The arghelper developers. All rights reserved.
# Project site: https://github.com/questrail/arghelper
# Use of this source code is governed by a MIT-style license that
# can be found in the LICENSE.txt file for the project.
"""Unit tests for arghelper.py."""

import argparse
import os
import sys
import unittest
from unittest import mock

import arghelper

TESTS_DIR = os.path.dirname(os.path.realpath(__file__))


class ExtantFixtures:
    """Paths shared by the extant_* test cases.

    This is a plain mixin rather than a TestCase subclass so that the cases
    below inherit the fixtures without also re-running each other's tests.
    """

    def setUp(self):
        self.existing_dir = os.path.join(TESTS_DIR, "existing_dir")
        self.non_existing_dir = os.path.join(TESTS_DIR, "non_existing_dir")
        self.existing_file = os.path.join(TESTS_DIR, "existing_file.txt")
        self.non_existing_file = os.path.join(TESTS_DIR, "non_existing_file.txt")


class TestExtantItem(ExtantFixtures, unittest.TestCase):
    def test_extant_item_directory_exists(self):
        """Test that a directory exists"""
        self.assertEqual(
            arghelper.extant_item(self.existing_dir, "directory"), self.existing_dir
        )

    def test_extant_item_directory_does_not_exist(self):
        """Test that a non-existing directory doesn't exist"""
        self.assertRaises(
            argparse.ArgumentTypeError,
            arghelper.extant_item,
            self.non_existing_dir,
            "directory",
        )

    def test_extant_item_directory_not_file(self):
        """Test that an existing file doesn't exist as a directory"""
        self.assertRaises(
            argparse.ArgumentTypeError,
            arghelper.extant_item,
            self.existing_file,
            "directory",
        )

    def test_extant_item_file_exists(self):
        """Test that a file exists"""
        self.assertEqual(
            arghelper.extant_item(self.existing_file, "file"), self.existing_file
        )

    def test_extant_item_file_does_not_exist(self):
        """Test that a non-existing file doesn't exist"""
        self.assertRaises(
            argparse.ArgumentTypeError,
            arghelper.extant_item,
            self.non_existing_file,
            "file",
        )

    def test_extant_item_file_not_directory(self):
        """Test that an existing directory doesn't exist as a file"""
        self.assertRaises(
            argparse.ArgumentTypeError,
            arghelper.extant_item,
            self.existing_dir,
            "file",
        )

    def test_extant_item_unknown_arg_type(self):
        """Test that an unrecognized arg_type raises instead of returning None"""
        with self.assertRaises(ValueError):
            # The Literal annotation on arg_type is what pyright objects to
            # here, and objecting is correct: this call is the mistake the
            # annotation exists to catch. The runtime check is what protects
            # a caller who is not type checked, so it is still tested.
            arghelper.extant_item(
                self.existing_file,
                "flie",  # pyright: ignore[reportArgumentType]
            )

    def test_extant_item_error_message_names_the_item(self):
        """Test that the error message identifies the missing item"""
        with self.assertRaises(argparse.ArgumentTypeError) as ctx:
            arghelper.extant_item(self.non_existing_file, "file")
        self.assertIn(self.non_existing_file, str(ctx.exception))


class TestExtantDirectory(ExtantFixtures, unittest.TestCase):
    def test_extant_directory_exists(self):
        """Test that a directory exists"""
        self.assertEqual(arghelper.extant_dir(self.existing_dir), self.existing_dir)

    def test_extant_directory_does_not_exist(self):
        """Test that a non-existing directory doesn't exist"""
        self.assertRaises(
            argparse.ArgumentTypeError, arghelper.extant_dir, self.non_existing_dir
        )

    def test_extant_directory_not_file(self):
        """Test that an existing file doesn't exist as a directory"""
        self.assertRaises(
            argparse.ArgumentTypeError, arghelper.extant_dir, self.existing_file
        )


class TestExtantFile(ExtantFixtures, unittest.TestCase):
    def test_extant_file_exists(self):
        """Test that a file exists"""
        self.assertEqual(arghelper.extant_file(self.existing_file), self.existing_file)

    def test_extant_file_does_not_exist(self):
        """Test that a non-existing file doesn't exist"""
        self.assertRaises(
            argparse.ArgumentTypeError, arghelper.extant_file, self.non_existing_file
        )

    def test_extant_file_not_directory(self):
        """Test that an existing directory doesn't exist as a file"""
        self.assertRaises(
            argparse.ArgumentTypeError, arghelper.extant_file, self.existing_dir
        )


class TestParseConfigInputOutput(unittest.TestCase):
    def setUp(self):
        self.script_name = os.path.join(TESTS_DIR, "sample.py")
        self.config_file = os.path.join(TESTS_DIR, "config_file.csv")
        self.input_dir = os.path.join(TESTS_DIR, "input_dir")
        self.output_dir = os.path.join(TESTS_DIR, "output_dir")
        self.argv = [
            self.script_name,
            self.config_file,
            self.input_dir,
            self.output_dir,
        ]

    def test_parse_config_input_output(self):
        """Test the parse_config_input_output function"""
        args = arghelper.parse_config_input_output(self.argv)
        self.assertEqual(args.config_file, self.config_file)
        self.assertEqual(args.input_dir, self.input_dir)
        self.assertEqual(args.output_dir, self.output_dir)

    def test_parse_config_input_output_reads_sys_argv_when_args_is_none(self):
        """Test that sys.argv is read at call time, not at import time"""
        with mock.patch.object(sys, "argv", self.argv):
            args = arghelper.parse_config_input_output()
        self.assertEqual(args.config_file, self.config_file)
        self.assertEqual(args.input_dir, self.input_dir)
        self.assertEqual(args.output_dir, self.output_dir)

    def test_parse_config_input_output_missing_dir(self):
        """Test that a non-existing directory exits with a usage error"""
        argv = [
            self.script_name,
            self.config_file,
            os.path.join(TESTS_DIR, "non_existing_dir"),
            self.output_dir,
        ]
        with self.assertRaises(SystemExit) as ctx:
            arghelper.parse_config_input_output(argv)
        self.assertEqual(ctx.exception.code, 2)


class TestParseConfig(unittest.TestCase):
    def setUp(self):
        self.script_name = os.path.join(TESTS_DIR, "sample.py")
        self.config_file = os.path.join(TESTS_DIR, "config_file.csv")
        self.argv = [self.script_name, self.config_file]

    def test_parse_config(self):
        """Test the parse_config function"""
        args = arghelper.parse_config(self.argv)
        self.assertEqual(args.config_file, self.config_file)

    def test_parse_config_reads_sys_argv_when_args_is_none(self):
        """Test that sys.argv is read at call time, not at import time"""
        with mock.patch.object(sys, "argv", self.argv):
            args = arghelper.parse_config()
        self.assertEqual(args.config_file, self.config_file)

    def test_parse_config_missing_file(self):
        """Test that a non-existing config file exits with a usage error"""
        argv = [self.script_name, os.path.join(TESTS_DIR, "non_existing_file.txt")]
        with self.assertRaises(SystemExit) as ctx:
            arghelper.parse_config(argv)
        self.assertEqual(ctx.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
