from copy_pages.copy_pages import copy_pages
from copy_pages.cli import cli
import argparse


class CommandLineParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Parser for PDF")
        self.subparsers = self.parser.add_subparsers(
            title='Available commands',
            dest='command',
            required=True
        )

    def parse(self):
        return self.parser.parse_args()


def main():
    parser = CommandLineParser()
    cli(parser.subparsers)
    args = parser.parse()

    if args.command == "copy_pages":
        copy_pages(args.input_file, args.output_file, args.from_page, args.to_page)


if __name__ == "__main__":
    main()
