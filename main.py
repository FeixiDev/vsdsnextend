import argparse
import process_control


class argparse_operator:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='vsdsnextend')
        self.setup_parse()

    def setup_parse(self):
        sub_parser = self.parser.add_subparsers()

        self.parser.add_argument('-v',
                                 '--version',
                                 dest='version',
                                 help='Show current version',
                                 action='store_true')

        self.parser.set_defaults(func=self.main_usage)

    def perform_all_tests(self, args):
        self.parser.print_help()

    def main_usage(self, args):
        if args.version:
            print(f'Version: v1.0.0')
        else:
            obj = process_control.Control()

    def parser_init(self):
        args = self.parser.parse_args()
        args.func(args)


if __name__ == "__main__":
    cmd = argparse_operator()
    cmd.parser_init()
