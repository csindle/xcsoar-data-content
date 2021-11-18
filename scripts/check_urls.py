#!/bin/env python3
"""Check if the repository URLs are working."""

import sys
import requests


def main(repo_url: str) -> bool:
    """HTTP request all the URLs in the repo_url."""
    repository = requests.get(repo_url)

    rv = True
    for line in repository.iter_lines():
        decoded_line = line.decode("utf-8")
        if decoded_line.startswith("uri="):
            url = decoded_line[4:]
            req = requests.head(url, allow_redirects=True)
            print(url, req.status_code)
            if req.status_code != requests.codes.ok:
                print(f"ERROR HEADing: {url}. Status code: {req.status_code}")
                rv = False
    return rv


if __name__ == "__main__":
    url = "http://download.xcsoar.org/repository"
    if main(repo_url=url):
        print(f"Download success for all of the URIs in {url}.")
        sys.exit(0)

    print(f"Download FAILURE for some/all of the URIs in {url}.")
    sys.exit(1)
