#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11-03-2023 12:17 pm
# @Author  : bhaskar.uprety
# @File    : email

"""email File created on 11-03-2023"""
import os.path
import pathlib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from queue import Queue
from smtplib import SMTP
from threading import Thread

from jinja2 import Environment, FileSystemLoader


class Emailer:
    """Email sending queue"""

    def __init__(self, name):
        base = pathlib.Path(__file__).parent.absolute()
        template_path = os.path.join(base, 'email_template')
        env = Environment(loader=FileSystemLoader(template_path))
        # Load the Jinja2 template from a file
        self.__template = env.get_template("send_code.html")
        self.__image_path = os.path.join(template_path, 'email.png')
        self.__mail_data = None
        self._stop = False
        self.operations = {
            'verify': self.__email_verification_message,
            'reset': self.__password_reset_message,
            'otp': self.__login_otp_message
        }
        self.user = os.getenv('SMTP_EMAIL')
        self.name = name
        self.message_queue = Queue()
        self.smtp: SMTP = SMTP(os.getenv('SMTP_SERVER'))
        Thread(target=self.__run).start()

    def __login(self):
        """login to smtp server"""
        self.smtp: SMTP = SMTP('smtp.gmail.com')
        self.smtp.starttls()
        self.smtp.login(self.user, os.getenv('SMTP_PASSWD'))
        self.smtp.noop()

    def stop(self):
        """Stop the queue"""
        self._stop = True

    def __generate_email_message(self, subject, to_email, title, name, token):
        """Generate an html email string based on given data"""
        email = MIMEMultipart("alternative")
        email['Subject'] = subject
        email['From'] = f'{self.name} <{self.user}>'
        email['To'] = to_email

        # Attach email image for html
        image_name = 'email'
        with open(self.__image_path, 'rb') as f:
            img_data = f.read()

        img = MIMEImage(img_data, name=image_name)
        img.add_header('Content-ID', f'<{image_name}>')
        email.attach(img)

        # Add a text version of email
        text_content = f'{title}. {name} is {token}'
        text_part = MIMEText(text_content)
        email.attach(text_part)

        # Add a html version of email
        html_content = self.__template.render(title=title, name=name, token=token)
        html_part = MIMEText(html_content, "html")
        email.attach(html_part)

        return email

    def __email_verification_message(self, data):
        """Verify user"""
        to_email = data['to_email']
        token = data['token']
        subject = 'Verify your email'
        title = "Please verify your email"
        name = 'Verification Code'
        email = self.__generate_email_message(subject, to_email, title, name, token)
        return email

    def __password_reset_message(self, data):
        """Verify user"""
        to_email = data['to_email']
        token = data['token']
        subject = 'Account recovery'
        title = "Recover your account"
        name = 'Recovery Code'
        email = self.__generate_email_message(subject, to_email, title, name, token)
        return email

    def __login_otp_message(self, data):
        """Verify user"""
        to_email = data['to_email']
        token = data['token']
        subject = 'OTP For login'
        title = "Authorize your session"
        name = 'Login OTP'
        email = self.__generate_email_message(subject, to_email, title, name, token)
        return email

    # noinspection PyBroadException
    def __send_message(self, message):
        """Send the given message"""
        try:
            self.smtp.send_message(message)
            print('email sent')
            return True
        except Exception:
            self.__login()
            return False

    def send_verification_email(self, to_email: str, token: str):
        """Send verification email"""
        data = {
            'token': token,
            'to_email': to_email,
            'operation': 'verify'
        }
        self.message_queue.put(data)

    def __run(self):
        """Run the process in infinite loop"""
        attempt = 0
        while not self._stop:
            if not self.__mail_data:
                self.__mail_data = self.message_queue.get()
            operation = self.__mail_data['operation']
            message = self.operations[operation](self.__mail_data)
            done = self.__send_message(message)
            attempt += 1
            if done and attempt <= 3:
                self.__mail_data = None
                attempt = 0
