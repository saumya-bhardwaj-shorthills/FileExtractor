import unittest
from extractors.data_extractor import DataExtractor
from unittest.mock import patch, MagicMock

class TestDataExtractor(unittest.TestCase):

    @patch('PyPDF2.PdfReader')
    def test_extract_text(self, mock_pdf_reader):
        # Mocking the PDF reader behavior
        mock_pdf = MagicMock()
        mock_pdf.pages = [MagicMock()]
        mock_pdf.pages[0].extract_text.return_value = "Test PDF content"
        mock_pdf_reader.return_value = mock_pdf
        
        extractor = DataExtractor("dummy.pdf")
        text = extractor.extract_text()

        self.assertEqual(text, "Test PDF content")

    @patch('camelot.read_pdf')
    def test_extract_tables(self, mock_camelot):
        # Mocking Camelot behavior for table extraction
        mock_table = MagicMock()
        mock_table.df = MagicMock()
        mock_table.df.values.tolist.return_value = [['Header1', 'Header2'], ['Data1', 'Data2']]
        mock_camelot.return_value = [mock_table]

        extractor = DataExtractor("dummy.pdf")
        tables = extractor.extract_tables()

        self.assertEqual(len(tables), 1)
        self.assertEqual(tables[0].df.values.tolist(), [['Header1', 'Header2'], ['Data1', 'Data2']])

    @patch('extractors.data_extractor.SQLStorage')
    def test_save_tables_to_sql(self, mock_sql_storage):
        # Mocking SQL storage
        mock_table = MagicMock()
        mock_table.df = MagicMock()
        mock_table.df.values.tolist.return_value = [['Header1', 'Header2'], ['Data1', 'Data2']]

        extractor = DataExtractor("dummy.pdf")
        extractor.extract_tables = MagicMock(return_value=[mock_table])

        mock_storage_instance = mock_sql_storage.return_value
        extractor.save_tables_to_sql("dummy.db")

        mock_storage_instance.save.assert_called_once()

if __name__ == '__main__':
    unittest.main()
