"""Module handling the initial DVWA security portal"""
import requests

from dvwa.base import Base


class Security(Base):
    """Class handling the initial DVWA security portal"""

    def __init__(self):
        super().__init__()

    @property
    def sec_url(self):
        """Property representing DVWA security URL"""

        return f"{self.base_url}/security.php"

    def _post_security_form(self, level):
        """Perform the POST request to the security portal"""

        security_response = self._get_security_page()
        
        csrf_token = self._extract_csrf_token(security_response)
        payload = self._build_security_payload(csrf_token, level)

        request = self._build_request_kwargs(self.sec_url, payload=payload)
        post_security_response = requests.post(**request)

        return post_security_response

    def _get_security_page(self):
        """Perform initial GET request to security portal"""

        request = self._build_request_kwargs(self.sec_url, post=False)
        security_response = requests.get(**request)
        
        return security_response
