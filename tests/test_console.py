#!/usr/bin/python3
"""
Console tests
"""

import console
import inspect
import unittest
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """Contains tests for console"""

    @classmethod
    def setUpClass(cls):
        """test setup"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """test teardown"""
        del cls.consol

    def tearDown(self):
        """Remoeve file.json"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Test for Pep8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["console.py"])
        self.assertEqual(pep.total_errors, 0, 'fix Pep8')

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

if __name__ == "__main__":
    unittest.main()
