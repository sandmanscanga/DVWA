"""Module handling the DVWA application"""
import requests
from bs4 import BeautifulSoup

from dvwa.login import Login
from dvwa.security import Security
from dvwa.home import Home


class DVWA(Login, Security, Home):
    """Class handling the DVWA application"""

    def __init__(self):
        super().__init__()

    def login(self):
        """Log in to DVWA"""

        post_login_response = self._post_login_form()

        self._update_cookie(post_login_response)

    def set_security_level(self, security_level="low"):
        """Set the DVWA security level"""

        levels = ("low", "medium", "high", "impossible")
        if security_level not in levels:
            raise Exception(f"Invalid security level: {security_level}")

        post_security_response = self._post_security_form(security_level)

        self._update_cookie(post_security_response)

    def set_phpids_mode(self, mode="off"):
        """Sets the DVWA PHPIDS mode"""

        modes = ("on", "off")
        if mode not in modes:
            raise Exception(f"Invalid PHPIDS mode: {mode}")

        payload = {"phpids": mode}
        kwargs = {"post": False, "payload": payload}
        request = self._build_request_kwargs(self.sec_url, **kwargs)
        _ = requests.get(**request)

    def get_vulns(self):
        """Get vulnerability list from homepage"""

        homepage_reponse = self._get_homepage()

        soup = BeautifulSoup(homepage_reponse.text, "lxml")

        vulns = {}

        anchors = soup.findAll("ul")[1].findAll("a")
        for anchor in anchors:
            anchor_href = anchor.get("href")
            url = f"{self.base_url}/{anchor_href}"
            title = anchor.text.strip()
            vulns[title] = url

        return vulns
