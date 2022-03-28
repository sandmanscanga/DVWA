"""Module for loading the ping sweep argument parser"""
from definitions.ping_sweep.definitions import Definitions


class Loader:
    """Class for loading the ping sweep argument parser"""

    def __init__(self, argparse):
        self.argparse = argparse
        self.parser = None
        self.raw_args = None

    def build_parser(self):
        """Builds the argument parser"""

        self.parser = self.argparse.ArgumentParser()

    def load_arguments(self):
        """Loads definitions into argument parser"""

        for args, kwargs in self.gen_definitions():
            self.parser.add_argument(*args, **kwargs)

    def parse_args(self):
        """Parse raw arguments"""

        self.args = self.parser.parse_args()

        return self.args

    @staticmethod
    def gen_definitions():
        """Generates a list of argument definitions"""

        definitions_obj = Definitions()

        definitions = []
        for definition_obj in dir(definitions_obj):
            if not str(definition_obj).startswith("__"):
                definition = getattr(definitions_obj, definition_obj)
                yield definition()
