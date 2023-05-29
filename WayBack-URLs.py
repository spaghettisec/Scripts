#!/usr/bin/python3
from typing import List
from sys import stdin
from socket import gethostbyname
from urllib.request import urlopen
from ssl import _create_unverified_context

if __name__ == "__main__":
    if stdin.isatty():
        print("echo \"example.com\" | python3 WayBack-URLs.py")
    else:
        domains: List[str] = stdin.read().strip().split("\n")
        for domain in domains:
            try:
                gethostbyname(domain)
                request = urlopen(url=f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=txt&fl=original&collapse=urlkey&page=/", context=_create_unverified_context())
                urls: str = request.read().decode(encoding="utf-8", errors="ignore").strip()
                if len(urls) > 0:
                    print(urls)
            except:
                continue
