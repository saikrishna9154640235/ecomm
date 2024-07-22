from django.conf import settings
from django.core.mail import send_mail




def send_account_activation_email(email,email_token):
    subject="your account must be verified"
    from_email=settings.EMAIL_HOST_USER
    message=f'his  lick on the link to validate your account  http://127.0.0.1:8898/accounts/activate/{email_token}/ '
    send_mail(subject,message,from_email,[email]) 