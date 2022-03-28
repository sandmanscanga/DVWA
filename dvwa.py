"""Module to run the main process"""
import json

from vulns.sqli.sqli_blind import main as sqli_blind_main


def main():
    """Runs the main process"""

    sqli_blind_main()


if __name__ == "__main__":
    main()
