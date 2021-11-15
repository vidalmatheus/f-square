import re
import time

from django.conf import settings
from django.core.exceptions import ValidationError


def only_numbers(s):
    if not s:
        return s
    return re.sub('[^0-9]', '', s)


def only_alphanum(s):
    if not s:
        return s
    return re.sub('[^0-9A-Za-z]', '', s)


def is_only_alpha(s):
    return all(c.isalpha() or c == ' ' for c in s)


def sleep(n):
    if settings.SKIP_SLEEP:
        return
    else:
        return time.sleep(n)


def error_str(ex):
    if isinstance(ex, ValidationError):
        return '; '.join(ex.messages)
    else:
        return str(ex)
