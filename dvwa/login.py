"""Module handling the initial DVWA login portal"""
import requests

from dvwa.base import Base


class Login(Base):
    """Class handling the initial DVWA login portal"""

    def __init__(self):
        super().__init__()

    @property
    def login_url(self):
        """Property representing DVWA login URL"""

        return f"{self.base_url}/login.php"

    def _post_login_form(self):
        """Perform the POST request to the login portal"""

        initial_login_response = self._get_initial_login()

        self._update_cookie(initial_login_response)

        csrf_token = self._extract_csrf_token(initial_login_response)
        payload = self._build_login_payload(csrf_token)

        request = self._build_request_kwargs(self.login_url, payload=payload)
        post_login_response = requests.post(**request)

        return post_login_response

    def _get_initial_login(self):
        """Perform initial GET request to login portal"""
        
        request = self._build_request_kwargs(self.login_url, post=False)
        initial_login_response = requests.get(**request)

        return initial_login_response
