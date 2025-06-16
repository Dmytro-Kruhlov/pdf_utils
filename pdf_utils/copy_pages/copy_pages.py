from typing import NoReturn
import pymupdf
import os


def open_pdf(file_path: str) -> pymupdf.Document:
    """Open a PDF file and return a PyMuPDF Document object.

       Args:
           file_path (str): Path to the PDF file to open.

       Returns:
           pymupdf.Document: PyMuPDF Document object if successful.

       Raises:
           FileNotFoundError: If the specified PDF file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input PDF file not found: {file_path}")
    return pymupdf.open(file_path)


def copy_pages(input_pdf: str, output_pdf: str, from_page: int, to_page: int) -> None:
    """Copy a range of pages from one PDF file to another.

        This function extracts pages from the input PDF file and saves them to the output PDF file.
        If the output file already exists, it will be overwritten with the new content.

        Args:
            input_pdf (str): Path to the source PDF file.
            output_pdf (str): Path where the PDF file will be saved. If a file already exists at this path,
                            it will be overwritten.
            from_page (int): Starting page number (0-based index).
            to_page (int): Ending page number (0-based index).

        Raises:
            FileNotFoundError: If the input PDF file does not exist.
            ValueError: If page numbers are invalid or if from_page is greater than to_page.
            ValueError: "Output file path must be provided"
    """
    doc = open_pdf(input_pdf)

    if from_page < 0 or to_page >= doc.page_count:
        raise ValueError(f"Invalid page numbers. PDF has {doc.page_count} pages")
    if from_page > to_page:
        raise ValueError("From page cannot be greater than to page")

    new_doc = pymupdf.open()
    new_doc.insert_pdf(doc, from_page=from_page, to_page=to_page)
    if not output_pdf:
        raise ValueError("Output file path must be provided")
    new_doc.save(output_pdf)
    new_doc.close()
    doc.close()





