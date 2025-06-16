import pytest
from unittest.mock import patch, MagicMock
from pdf_utils.copy_pages.copy_pages import open_pdf, copy_pages


class TestOpenPDF:
    @patch("os.path.exists")
    @patch("pymupdf.open")
    def test_open_pdf_success(self, mock_pymupdf_open, mock_exists):
        file_path = "test.pdf"
        mock_exists.return_value = True
        mock_doc = MagicMock()
        mock_pymupdf_open.return_value = mock_doc

        result = open_pdf(file_path)

        mock_exists.assert_called_once_with(file_path)
        mock_pymupdf_open.assert_called_once_with(file_path)
        assert result == mock_doc

    @patch("os.path.exists")
    def test_open_pdf_file_not_found(self, mock_exists):
        file_path = "nonexistent.pdf"
        mock_exists.return_value = False

        with pytest.raises(FileNotFoundError) as exception:
            open_pdf(file_path)
        assert str(exception.value) == f"Input PDF file not found: {file_path}"
        mock_exists.assert_called_once_with(file_path)


class TestPDFCopyPages:
    def setup_method(self):
        self.input_pdf = "input.pdf"
        self.output_pdf = "output.pdf"

    @patch("pymupdf.open")
    @patch("pdf_utils.copy_pages.copy_pages.open_pdf")
    def test_pdf_copy_pages_success(self, mock_open_pdf, open_empty_pdf):
        from_page = 0
        to_page = 2

        mock_doc = MagicMock()
        mock_doc.page_count = 5
        mock_open_pdf.return_value = mock_doc

        mock_new_doc = MagicMock()
        open_empty_pdf.return_value = mock_new_doc

        copy_pages(self.input_pdf, self.output_pdf, from_page, to_page)

        mock_open_pdf.assert_called_once_with(self.input_pdf)
        open_empty_pdf.assert_called_once()
        mock_new_doc.insert_pdf.assert_called_once_with(
            mock_doc, from_page=from_page, to_page=to_page
        )
        mock_new_doc.save.assert_called_once_with(self.output_pdf)
        mock_new_doc.close.assert_called_once()
        mock_doc.close.assert_called_once()

    @patch("pdf_utils.copy_pages.copy_pages.open_pdf")
    def test_pdf_copy_pages_invalid_page_numbers(self, mock_open_pdf):
        from_page = -1
        to_page = 2

        mock_doc = MagicMock()
        mock_doc.page_count = 5
        mock_open_pdf.return_value = mock_doc

        with pytest.raises(ValueError) as exception:
            copy_pages(self.input_pdf, self.output_pdf, from_page, to_page)
        assert str(exception.value) == "Invalid page numbers. PDF has 5 pages"

    @patch("pdf_utils.copy_pages.copy_pages.open_pdf")
    def test_pdf_copy_pages_from_greater_than_to(self, mock_open_pdf):
        from_page = 3
        to_page = 1

        mock_doc = MagicMock()
        mock_doc.page_count = 5
        mock_open_pdf.return_value = mock_doc

        with pytest.raises(ValueError) as exception:
            copy_pages(self.input_pdf, self.output_pdf, from_page, to_page)
        assert str(exception.value) == "From page cannot be greater than to page"

    def test_pdf_copy_pages_empty_output_path(self):
        input_pdf = "data/test_data.pdf"
        output_pdf = ""
        from_page = 0
        to_page = 2

        # mock_doc = MagicMock()
        # mock_doc.page_count = 5
        # mock_open_pdf.return_value = mock_doc

        with pytest.raises(ValueError) as exception:
            copy_pages(input_pdf, output_pdf, from_page, to_page)
        assert str(exception.value) == "Output file path must be provided"
