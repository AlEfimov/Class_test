import unittest
from unittest.mock import patch, call


class Document:
    def __init__(self, printer_name):
        self._printer_name = printer_name


    def print_document(self):
        return self._printer_name.print_page()


class InkjetPrinter:
    def print_page(self):
        print("Печать на струйном принтере")


class LaserPrinter:
    def print_page(self):
        print("Печать на лазерном принтере")


class TetsDocument(unittest.TestCase):
    @patch('builtins.print')
    def test_print_document_for_InkjetPrinter(self, mock_print_document):
        Document(InkjetPrinter()).print_document()
        mock_print_document.assert_called_with('Печать на струйном принтере')


    @patch('builtins.print')
    def test_print_document_for_LaserPrinter(self, mock_print_document):
        Document(LaserPrinter()).print_document()
        mock_print_document.assert_called_with('Печать на лазерном принтере')


if __name__ == "__main__":
    unittest.main()