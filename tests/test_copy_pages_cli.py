import pytest
import argparse

from pdf_utils.copy_pages.cli import cli


@pytest.fixture
def parser():
    parser = argparse.ArgumentParser(prog='test')
    subparsers = parser.add_subparsers(dest='command')
    cli(subparsers)
    return parser


class TestCopyCli:

    def test_copy_parser_required(self, parser):

        with pytest.raises(SystemExit):
            parser.parse_args(['copy_pages'])

    def test_copy_parser_happy_path(self, parser):
        args = parser.parse_args([
            'copy_pages',
            '-i', 'input.pdf',
            '-o', 'output.pdf',
            '--from_page', '1',
            '--to_page', '5'
        ])

        assert args.command == 'copy_pages'
        assert args.input_file == 'input.pdf'
        assert args.output_file == 'output.pdf'
        assert args.from_page == 1
        assert args.to_page == 5

    def test_copy_parser_default_from_page(self, parser):
        args = parser.parse_args([
            'copy_pages',
            '-i', 'input.pdf',
            '-o', 'output.pdf',
            '--to_page', '5'
        ])

        assert args.from_page == 0

    def test_copy_parser_to_page_required(self, parser):
        with pytest.raises(SystemExit):
            parser.parse_args([
                'copy_pages',
                '-i', 'input.pdf',
                '-o', 'output.pdf'
            ])