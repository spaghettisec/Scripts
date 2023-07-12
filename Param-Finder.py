#!/usr/bin/python3
from urllib.parse import urlparse, urlencode, urlunparse, parse_qsl
from concurrent.futures import ThreadPoolExecutor
from requests.models import PreparedRequest
from urllib3 import disable_warnings
from typing import List, Union
from termcolor import colored
from sys import argv, stdin
from requests import get
from re import search

def getInputFieldName(html: str) -> Union[str, None]:
    regex = r'<input[^>]+name="([^"]+)"'
    match = search(regex, html)
    if match:
        name: str = match.group(1)
        return name
    else:
        return None

def detectReflect(param: str) -> None:
    try:
        req = PreparedRequest()
        req.prepare_url(url, {param: payload})
        if payload in get(req.url, headers=userAgent, verify=False).text:
            print(req.url)
    except:
        pass
    
def help() -> None:
    print("echo \"https://www.example.com/\" | python3 Param-Finder \"Payload\" Threads (1-100)")

def main() -> None:
    try:
        response: str = get(url, headers=userAgent, verify=False).text
        for line in response.split(">"):
            if "<input" in line:
                params.add(getInputFieldName(line))
                for param in list(params):
                    pool.submit(detectReflect, param)
    except:
        pass
if __name__ == "__main__":
    if stdin.isatty():
        help()
    else:
        try:
            disable_warnings()
            payload: str = argv[1]
            threads: int = int(argv[2])
            pool = ThreadPoolExecutor(max_workers=threads)
            params: set = set()
            urls: List[str] = stdin.read().strip().split("\n")
            userAgent: dict = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
            for url in urls:
                main()
        except IndexError:
            help()
        except Exception as error:
            print(error)
