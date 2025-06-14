import argparse
from pdf_copy_pages import pdf_copy_pages


class CommandLineParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Parser for PDF")
        self.subparsers = self.parser.add_subparsers(
            title='Available commands',
            dest='command',
            required=True
        )
        self._add_copy_pages_subparser()

    def _add_copy_pages_subparser(self):
        copy_parser = self.subparsers.add_parser(
            "copy_pages",
            help="Copy pages from PDF file"
        )
        copy_parser.add_argument("-i", "--input_file", help="path to input file", required=True)
        copy_parser.add_argument("-o", "--output_file", help="path to output file", required=True)
        copy_parser.add_argument("--from_page", help="start page", type=int, default=0)
        copy_parser.add_argument("--to_page", help="finish page", type=int, required=True)

    def parse(self):
        return self.parser.parse_args()


def main():
    parser = CommandLineParser()
    args = parser.parse()

    if args.command == "copy_pages":
        pdf_copy_pages(args.input_file, args.output_file, args.from_page, args.to_page)


if __name__ == "__main__":
    main()