
def cli(subparsers):
    copy_parser = subparsers.add_parser(
        "copy_pages",
        help="Copy pages from PDF file"
    )
    copy_parser.add_argument("-i", "--input_file", help="path to input file", required=True)
    copy_parser.add_argument("-o", "--output_file", help="path to output file", required=True)
    copy_parser.add_argument("--from_page", help="start page", type=int, default=0)
    copy_parser.add_argument("--to_page", help="finish page", type=int, required=True)
