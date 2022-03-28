"""Module handling the DVWA application home"""
import requests

from dvwa.base import Base


class Home(Base):
    """Class handling the DVWA application home"""

    def __init__(self):
        super().__init__()

    @property
    def home_url(self):
        """Property representing DVWA homepage URL"""

        return f"{self.base_url}/index.php"

    def _get_homepage(self):
        """Gets the DVWA homepage"""

        request = self._build_request_kwargs(self.home_url, post=False)
        homepage_response = requests.get(**request)

        return homepage_response
