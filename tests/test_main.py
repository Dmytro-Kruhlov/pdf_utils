from unittest.mock import patch, MagicMock
from pdf_utils import main


class TestMain:

    def test_main_copy_pages_called(self):

        mock_args = MagicMock()
        mock_args.command = "copy_pages"
        mock_args.input_file = "input.pdf"
        mock_args.output_file = "output.pdf"
        mock_args.from_page = 1
        mock_args.to_page = 5

        with patch.object(main.CommandLineParser, "parse", return_value=mock_args), patch.object(main, "copy_pages") as mock_copy:

            main.main()

            mock_copy.assert_called_once_with("input.pdf", "output.pdf", 1, 5)

    def test_main_invalid_command(self):

        mock_args = MagicMock()
        mock_args.command = "foo"

        with patch.object(main.CommandLineParser, "parse", return_value=mock_args), patch.object(main, "copy_pages") as mock_copy:

            main.main()

            mock_copy.assert_not_called()