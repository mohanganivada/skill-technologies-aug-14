import threading
import secrets
import random
from threading import Thread
from skill import settings as ES
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import urllib.request
import urllib.parse
import datetime
import json
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, ES.EMAIL_HOST_USER, self.recipient_list)
        #msg.content_subtype = "html"
        msg.send()

def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()

    
