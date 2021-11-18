#!/bin/env python3
""""""

from pathlib import Path
import sys
import requests


def main() -> bool:
    """ """
    r = requests.get("http://download.xcsoar.org/repository")
    for line in r.iter_lines():
        # filter out keep-alive new lines
        if line:
            decoded_line = line.decode("utf-8")
            if decoded_line.startswith("uri"):
                url = line[4:]

                c = requests.head(url, allow_redirects=True)
                # print(url, c.status_code)
                if c.status_code != requests.codes.ok:
                    print(f"ERROR getting: {url}. Status code: {c.status_code}")


if __name__ == "__main__":
    # json_file = Path(sys.argv[1])

    if main():
        sys.exit(0)
    sys.exit(1)
