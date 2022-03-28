"""Module handling the base functionality of the DVWA application"""
from copy import deepcopy
import json

from bs4 import BeautifulSoup

from config.config import Config


class Base:
    """Class handling the base functionality of the DVWA application"""

    def __init__(self):
        self.cookie = {}

    @property
    def base_url(self):
        """Property representing the DVWA base URL"""

        return f"http://{Config.target}"

    def _update_cookie(self, response):
        """Updates instance internal cookie from response"""

        self.cookie.update(response.cookies.get_dict())

    def _build_request_kwargs(self, url, post=True, payload=None):
        """Builds requests kwargs dictionary"""

        request = {}
        request["url"] = url
        request["cookies"] = self.cookie
        request["allow_redirects"] = False
        if post is True:
            request["data"] = payload
        else:
            request["params"] = payload

        return deepcopy(request)

    @staticmethod
    def _display_response(response, text=False):
        """Display the response for debugging"""

        result = {}
        result["status_code"] = response.status_code
        result["headers"] = dict(response.headers.items())
        result["cookies"] = response.cookies.get_dict()
        if text is True:
            result["data"] = response.text

        print(json.dumps(result))

    @staticmethod
    def _extract_csrf_token(response):
        """Extracts CSRF token from initial login portal response"""

        soup = BeautifulSoup(response.text, "lxml")

        form = soup.find("form")
        token_handle = {"name": "user_token"}
        token_field = form.find("input", token_handle)
        csrf_token = token_field.get("value")

        return csrf_token

    @staticmethod
    def _build_login_payload(token):
        """Builds the payload for the login POST form"""

        payload = {}
        payload["username"] = Config.login_username
        payload["password"] = Config.login_password
        payload["Login"] = "Login"
        payload["user_token"] = token

        return deepcopy(payload)

    @staticmethod
    def _build_security_payload(token, level):
        """Builds the payload for the security POST form"""

        payload = {}
        payload["security"] = level
        payload["seclev_submit"] = "Submit"
        payload["user_token"] = token

        return deepcopy(payload)
