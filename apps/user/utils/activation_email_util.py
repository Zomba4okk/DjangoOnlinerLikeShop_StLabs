from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .activation_token_util import ActivationTokenUtil


class ActivationEmailUtil:
    @staticmethod
    def send_activation_email(user):
        send_mail(
            'Account activation',
            '...',
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=render_to_string(
                'activation_email.html',
                {'link':
                    f'{settings.USER_ACTIVATION_URI}'
                    f'{ActivationTokenUtil.get_encrypted_token_string(user.id)}'}  # noqa
            )
        )
