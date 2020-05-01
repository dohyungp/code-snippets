#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
from re import match

PATTERN = r'(?P<datetime>[\d+/ :]+) \[(?P<errortype>.+)\] .*?: (?P<errormessage>.+), client: (?P<client>.+), server: (?P<server>.+), request: (?P<request>.+), host: (?P<host>.+)'


def convert_nginx_log_to_dict():
    """Read from command line using pipe(|) and convert nginx log to json file

    Returns:
        list -- nginx log json
    """
    nginx_logs = list()
    lines = sys.stdin.readlines()
    if not lines:
        return nginx_logs

    for line in lines:
        pattern = match(PATTERN, line)
        log = pattern.groupdict()
        nginx_logs.append(log)

    return nginx_logs
