#!/bin/env python3
"""Check if all the repository URLs are working."""

import sys
import requests
from typing import List


def get_urls(repo_url: str) -> List[str]:
    """Extract all the URLs after "uri=" at repo_url."""
    repo_req = requests.get(repo_url)

    urls = []
    for line in repo_req.iter_lines():
        decoded_line = line.decode("utf-8")
        if decoded_line.startswith("uri="):
            urls.append(decoded_line[4:])
    return urls


def check_urls(urls: List[str]) -> bool:
    """Check (by an HTTP HEAD request) the URLs in urls."""
    rv = True
    for i, url in enumerate(urls):
        req = requests.head(url, allow_redirects=True)
        if req.status_code == requests.codes.ok:
            print(f"{i}\tpass {req.status_code} {url}")
        else:
            print(f"{i}\tFAIL {req.status_code} {url}\t!!!")
            rv = False
    return rv


if __name__ == "__main__":

    repository = "http://download.xcsoar.org/repository"

    if check_urls(urls=get_urls(repo_url=repository)):
        print(f"Download success for all of the URIs in {repository}.")
        sys.exit(0)

    print(f"Download FAILURE for some/all of the URIs in {repository}.")
    sys.exit(1)
