#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo


# Your test case class goes here
class TestEcho(unittest.TestCase):

    def setU(self):
        pass

    def test_upper_short(self):
        # self.fail("You need to write this test")
        args = ["-u", "hello world"]
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_lower_short(self):
        args = ["-l", "HelLo WorLD"]
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_title_short(self):
        args = ["-t", "HelLo WorLD"]
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_upper_long(self):
        self.fail("You need to write this test")

    def test_lower_long(self):
        self.fail("You need to write this test")

    def test_title_long(self):
        self.fail("You need to write this test")


if __name__ == '__main__':
    unittest.main()
