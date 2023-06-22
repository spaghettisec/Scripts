#!/usr/bin/python3
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from sys import argv, stdin
from typing import List

def getParameterNames(url) -> List[str]:
    parsedURL = urlparse(url)
    query = parsedURL.query.strip('?')
    parameterNames: List[str] = [param.split('=')[0] for param in query.split('&')]
    return parameterNames

def replaceParameter(url: str, parameter: str, replace: str) -> str:
    parsedURL = urlparse(url)
    queryParams = parse_qs(parsedURL.query, keep_blank_values=True)

    for param in queryParams:
        if param == parameter:
            queryParams[param] = [replace]

    newQueryString = urlencode(queryParams, doseq=True)
    newParsedURL = parsedURL._replace(query=newQueryString)
    newURL = urlunparse(newParsedURL)

    return newURL

if __name__ == "__main__":
    if stdin.isatty():
        print("echo \"https://google.com/?search=example\" | python3 Param-Replace.py \"replace\"")
    else:
        urls: List[str] = stdin.read().strip().split("\n")
        for url in urls:
            parameters: List[str] = getParameterNames(url)
            for parameter in parameters:
                print(replaceParameter(url, parameter, argv[1]))