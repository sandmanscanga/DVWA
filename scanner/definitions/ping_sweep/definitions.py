"""Module containing argument definitions for ping sweep"""
from definitions.ping_sweep.help import Help


class Definitions:
    """Class containing ping sweep definitions"""

    def cidr(self):
        """CIDR of the network scan"""

        args = ("-c", "--cidr")
        kwargs = dict(
            dest="cidr",
            metavar="cidr",
            required=False,
            type=int,
            default=24,
            help=Help.cidr
        )

        return args, kwargs

    def dhcp(self):
        """IP address of the DHCP of the network to scan"""

        args = ("-d", "--dhcp")
        kwargs = dict(
            dest="dhcp",
            metavar="dhcp",
            required=False,
            type=str,
            default="192.168.56.100",
            help=Help.dhcp
        )

        return args, kwargs

    def router(self):
        """IP address of the router of the network to scan"""
        args = ("-r", "--router")
        kwargs = dict(
            dest="router",
            metavar="router",
            required=False,
            type=str,
            default="192.168.56.1",
            help=Help.router
        )

        return args, kwargs

    def attacker(self):
        """IP address of the attacker of the network scan"""

        args = ("-a", "--attacker")
        kwargs = dict(
            dest="attacker",
            metavar="attacker",
            required=False,
            type=str,
            default="192.168.56.101",
            help=Help.attacker
        )

        return args, kwargs

    def target(self):
        """IP address of the target to scan"""

        args = ("-t", "--target")
        kwargs = dict(
            dest="target",
            metavar="target",
            required=False,
            type=str,
            help=Help.target
        )

        return args, kwargs

    def network(self):
        """IP address of the network to scan"""

        args = ("-n", "--network")
        kwargs = dict(
            dest="network",
            metavar="network",
            required=False,
            type=str,
            default="192.168.56.0",
            help=Help.network
        )

        return args, kwargs

    def verbose(self):
        """Verbose flag"""

        args = ("-v", "--verbose")
        kwargs = dict(
            dest="verbose",
            action="store_true",
            help=Help.verbose
        )

        return args, kwargs

    def debug(self):
        """Debug flag"""

        args = ("--debug",)
        kwargs = dict(
            dest="debug",
            action="store_true",
            help=Help.debug
        )

        return args, kwargs

    def silent(self):
        """Silent flag"""

        args = ("--silent",)
        kwargs = dict(
            dest="silent",
            action="store_true",
            help=Help.silent
        )

        return args, kwargs
