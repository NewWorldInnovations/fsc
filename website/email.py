from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def send_confirmation_email(new_user, domain, to_email):
    
	message = render_to_string('email_confirmation.html', 
								{'user': new_user, 
								'domain': domain,
								'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),
                				'token':account_activation_token.make_token(new_user),
            					})
	email = EmailMessage("Confirm Your Email Address", message, to=[to_email])
	email.send()

