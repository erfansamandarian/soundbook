import argparse

from soundbook.core.handler import Config
from soundbook.core.runner import Runner


def arguments():
    parser = argparse.ArgumentParser(
        prog="soundbook", description="search, download, and merge audiobooks"
    )
    parser.add_argument(
        "--book",
        help="The name of the audiobook you want to download",
    )
    parser.add_argument(
        "--url",
        help="The URL of the audiobook you want to download",
    )
    args = parser.parse_args()
    return Config(args)


def main():
    config = arguments()
    Runner(config).run()
