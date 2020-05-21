import os
from typing import List
from requests import Response, post

class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message

class Mailgun:
    FROM_TITLE = "Pricing alert service"
    FROM_EMAIL = "do-not-reply@sandboxb45710babc5b42fe9b974eda2f73c86b.mailgun.org"

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        mailgun_api_key = os.environ.get("MAILGUN_API_KEY", None)
        mailgun_domain = os.environ.get("MAILGUN_DOMAIN", None)
        if mailgun_api_keyY is None:
            raise MailgunException("Fail to load Mailgun API key")

        if mailgun_domain is None:
            raise MailgunException("Fail to load Mailgun domain")
        response = post(
                    f"{mailgun_domain}/messages",
                    auth=("api", mailgun_api_key),
                    data={
                        "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                        "to": email,
                        "subject": subject,
                        "text": txet,
                        "html": html})

        if response.status_code != 200:
            raise MailgunException("An error occurred while sending e-mail.")

        return response
