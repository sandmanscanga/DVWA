"""Module for performing a stealth scan"""
import json

import nmap


class StealthScan:
    """Class defining the stealth scan"""

    def __init__(self, **kwargs):
        self.target = kwargs.get("target")
        self.port_single = kwargs.get("port_single")
        self.port_multi = kwargs.get("port_multi")
        self.port_range = kwargs.get("port_range")
        self.verbose = kwargs.get("verbose")
        self.debug = kwargs.get("debug")

    def get_open_ports(self):
        """Gets the open ports from the stealth scan"""

        pass

    def display(self):
        """Displays debug info about object"""

        print(json.dumps(self.__dict__, indent=2))


def main(**kwargs):
    """Runs the main function"""

    client = StealthScan(**kwargs)
    if kwargs.get("debug"):
        print("[*] Displaying raw arguments")
        client.display()

    if kwargs.get("verbose") or kwargs.get("debug"):
        print("[*] Running stealth scan")
    
    ports = client.get_open_ports()
    
    if kwargs.get("verbose") or kwargs.get("debug"):
        print(f"[+] Found: {ports}")
    else:
        print(ports)


if __name__ == "__main__":
    import argparse

    from definitions.stealth_scan.loader import Loader

    loader = Loader(argparse)
    loader.build_parser()
    loader.load_arguments()
    args = loader.parse_args()
    kwargs = dict(args._get_kwargs())

    main(**kwargs)
