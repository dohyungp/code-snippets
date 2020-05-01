#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import search
import sys
import os
import fnmatch
import json
from slacker import Slacker

TOKEN = os.getenv('SLACK_TOKEN')
SLACK_CHANNEL = os.getenv('SLACK_CRON_CHANNEL')
if not TOKEN:
    sys.exit()


def find_user_code(text, directory='/var/www/', file_type='py'):
    pattern = rf'{directory}(\w+|-|_)+/(\w+|-|_)+.{file_type}'
    user_code = search(pattern, text)

    if user_code:
        user_code = user_code.group(0)

    return user_code


def read_in():
    lines = ''.join(sys.stdin.readlines())

    if 'Traceback' not in lines:
        return None, None

    code = find_user_code(lines)

    return lines, code


def send_error_to_slack(message, code):
    title = code or 'anonymous'
    slack = Slacker(TOKEN)
    attachments = json.dumps(
        [{'color': '#e00505', 'title': title, 'text': message}])
    slack.chat.post_message(SLACK_CHANNEL, '', username='Cron warning Bot',
                            as_user=False, attachments=attachments, icon_emoji=':warning:')


def main():
    """Usage
    $ chmod +x /var/www/cronjob_error_listener.py
    $ crontab -e 

    and then write on the configure file as following as:

    * * * * *  /usr/bin/python3 some_a_python_script.py | tee -a some_a_log_file.log | /var/www/cronjob_error_listener.py
    """
    lines, code = read_in()

    if lines is not None:
        send_error_to_slack(lines, code)


if __name__ == '__main__':
    main()
