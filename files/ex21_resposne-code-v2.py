#!/usr/bin/env python3

"""
    Open HTTP server log file. Summarize how many requests resulted in numeric response codes.
    - We use Counter to count the response code - https://github.com/reuven/python-workout/blob/master/ch05-files/e21b3_response_counts.py
    - also a good reference to encode and decode from HTTP Requests
"""

import requests
from pprint import pprint
from collections import Counter


def get_status_line_code(line):
    """Return the status code from the given line."""

    strip_line = line.strip()
    code = strip_line.split()[8]
    return code


if __name__ == "__main__":
    log_url = "https://gist.githubusercontent.com/reuven/5875971/raw/0f20d30d9457c1ded3c6c82798946afaf0b82292/mini-access-log.txt"
    response = requests.get(log_url)

    # Note:
    # - You can specify the decoding options to process reponse by providing the encoding parameter. e.g. response.encoding = "utf-8"
    # - The encoding parameter allows you to specify the character encoding to be used when decoding the response content.
    # - By default, response.text will try to determine the encoding based on the HTTP *response* headers (e.g., Content-Type)
    # - that the response.encoding attribute is set automatically by requests based on the information provided in the *response* headers.
    content_type = response.headers.get("Content-Type")
    encoding = response.encoding
    print("Content-Type:", content_type)                        # Content-Type: text/plain; charset=utf-8
    print("Encoding:", encoding)                                # Encoding: utf-8

    if response.status_code == 200:
        response.encoding = "utf-8"                             # Explicitely specify the desired encoding
        # Read the content of the file
        log = response.text
        count = Counter(get_status_line_code(line) for line in log.splitlines() if not line.startswith(("#", "\n")))
        pprint(count)
        pprint(f"Total: {count.total()}")
    else:
        print(f"Error: Filed to fetch the file contents from give url: {log_url}!")
