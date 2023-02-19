import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    MAIL_SERVER="sandbox.smtp.mailtrap.io"
    MAIL_PORT=465 # you may need to change this to 25, 587 or 2525
    MAIL_USERNAME="0fb17b9789b004"
    MAIL_PASSWORD="1c3c96a1f8378a"
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')

"""
Host:
sandbox.smtp.mailtrap.io
Port: 25 or 465 or 587 or 2525
Username: 0fb17b9789b004
Password: 1c3c96a1f8378a
Auth: PLAIN, LOGIN and CRAM-MD5
TLS: Optional (STARTTLS on all ports)
"""
