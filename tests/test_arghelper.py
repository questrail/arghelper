# -*- coding: utf-8 -*-
# Copyright (c) 2014 The arghelper developers. All rights reserved.
# Project site: https://github.com/matthewrankin/arghelper
# Use of this source code is governed by a MIT-style license that
# can be found in the LICENSE.txt file for the project.
"""Unit tests for arghelper.py.
"""
import argparse
import os
import unittest
import arghelper


class TestExtantItem(unittest.TestCase):

    def setUp(self):  # NOQA
        self.existing_dir = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'existing_dir')

        self.non_existing_dir = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'non_existing_dir')

        self.existing_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'existing_file.txt')

        self.non_existing_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'non_existing_file.txt')

    def test_extant_item_directory_exists(self):
        """Test that a directory exists"""
        self.assertEqual(
            arghelper.extant_item(self.existing_dir, "directory"),
            self.existing_dir)

    def test_extant_item_directory_does_not_exist(self):
        """Test that a non-existing directory doesn't exist"""
        self.assertRaises(
            argparse.ArgumentError,
            arghelper.extant_item,
            self.non_existing_dir,
            "directory")

    def test_extant_item_directory_not_file(self):
        """Test that an existing file doesn't exist as a directory"""
        self.assertRaises(
            argparse.ArgumentError,
            arghelper.extant_item,
            self.existing_file,
            "directory")

    def test_extant_item_file_exists(self):
        """Test that a file exists"""
        self.assertEqual(
            arghelper.extant_item(self.existing_file, "file"),
            self.existing_file)

    def test_extant_item_file_does_not_exist(self):
        """Test that a non-existing file doesn't exist"""
        self.assertRaises(
            argparse.ArgumentError,
            arghelper.extant_item,
            self.non_existing_file,
            "file")

    def test_extant_item_file_not_directory(self):
        """Test that an existing directory doesn't exist as a file"""
        self.assertRaises(
            argparse.ArgumentError,
            arghelper.extant_item,
            self.existing_dir,
            "file")


class TestExtantDirectory(TestExtantItem):

    def test_extant_directory_exists(self):
        """Test that a directory exists"""
        self.assertEqual(
            arghelper.extant_dir(self.existing_dir),
            self.existing_dir)

    def test_extant_directory_does_not_exist(self):
        """Test that a non-existing directory doesn't exist"""
        self.assertRaises(
            argparse.ArgumentError,
            arghelper.extant_dir,
            self.non_existing_dir)

    def test_extant_directory_not_file(self):
        """Test that an existing file doesn't exist as a directory"""
        self.assertRaises(
            argparse.ArgumentError,
            arghelper.extant_dir,
            self.existing_file)


class TestExtantFile(TestExtantItem):

    def test_extant_file_exists(self):
        """Test that a file exists"""
        self.assertEqual(
            arghelper.extant_file(self.existing_file),
            self.existing_file)

    def test_extant_file_does_not_exist(self):
        """Test that a non-existing file doesn't exist"""
        self.assertRaises(
            argparse.ArgumentError,
            arghelper.extant_file,
            self.non_existing_file)

    def test_extant_file_not_directory(self):
        """Test that an existing directory doesn't exist as a file"""
        self.assertRaises(
            argparse.ArgumentError,
            arghelper.extant_file,
            self.existing_dir)

if __name__ == '__main__':
    unittest.main()
