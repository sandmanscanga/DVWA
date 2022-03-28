"""Module for performing a ping sweep"""
import json

import nmap


class PingSweep:
    """Class defining the ping sweep"""

    def __init__(self, **kwargs):
        self.cidr = kwargs.get("cidr")
        self.dhcp = kwargs.get("dhcp")
        self.router = kwargs.get("router")
        self.attacker = kwargs.get("attacker")
        self.target = kwargs.get("target")
        self.network = kwargs.get("network")

    def _get_targets(self):
        """Gets a list of target IP addresses"""

        scanner = nmap.PortScanner()
        scanner.scan(hosts=f"{self.network}/{self.cidr}", arguments="-sn")

        targets = []
        for host in scanner.all_hosts():
            if host not in (self.dhcp, self.router, self.attacker):
                targets.append(host)

        if not len(targets):
            raise Exception("[!] No targets found")

        return targets, scanner

    def get_target(self):
        """Gets the target IP using a ping sweep"""

        scanner = None
        if self.target is None:
            targets, scanner = self._get_targets()
            if len(targets) > 1:
                raise Exception("[!] More than one target found")

            self.target = targets.pop()

        result = scanner[self.target]

        return result

    def display(self):
        """Displays debug info about object"""

        print(json.dumps(self.__dict__, indent=2))


def main(**kwargs):
    """Runs the main function"""

    client = PingSweep(**kwargs)
    if kwargs.get("debug"):
        print("[*] Displaying raw arguments")
        client.display()

    if kwargs.get("verbose") or kwargs.get("debug"):
        print("[*] Running ping sweep")

    result = client.get_target()
    
    if kwargs.get("verbose") or kwargs.get("debug"):
        print(f"[+] Found: {json.dumps(result, indent=2)}")
    else:
        if kwargs.get("silent") is False:
            print(json.dumps(result, indent=2))


if __name__ == "__main__":
    import argparse

    from definitions.ping_sweep.loader import Loader

    loader = Loader(argparse)
    loader.build_parser()
    loader.load_arguments()
    args = loader.parse_args()
    kwargs = dict(args._get_kwargs())

    main(**kwargs)
