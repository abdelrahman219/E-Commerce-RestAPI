from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail

def send_email(subject, message, from_email, recipient_list):
    html_content = message
    msg = EmailMultiAlternatives(subject, '', from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
   