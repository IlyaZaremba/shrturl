from django.core.exceptions import ValidationError
import re

url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


class UrlRegexValidator:
    """Regular Expression Validation."""

    @staticmethod
    def validate_url(url, error=None):
        """Validate url."""
        error = error if error is not None else ValidationError(message='Invalid url!')
        match_obj = re.match(url_regex, url)
        if not match_obj or match_obj.endpos != len(url):
            raise error
        return True
