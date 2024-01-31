from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_invitation(to_email,team):
    from_email = settings.DEFAULT_FROM_EMAIL
    acceptation_url = settings.ACCEPTATION_URL

    subject = 'Invitation to KanisaOS'
    text_context = 'Invitation Kanisaos.'
    html_content = render_to_string('users/email_invitation.html',{'team':team,'acceptation_url':acceptation_url})

    msg = EmailMultiAlternatives(subject,text_context,from_email,[to_email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


