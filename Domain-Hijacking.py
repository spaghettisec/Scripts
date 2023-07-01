#!/usr/bin/python3
from typing import List
from sys import argv, stdin
from termcolor import colored
from socket import gethostbyname
from dns.resolver import resolve, query, NXDOMAIN

def NXDomain(domain: str) -> bool:
    try:
        resolve(domain)
        return False
    except NXDOMAIN:
        return True

if __name__ == '__main__':
    if stdin.isatty():
        print("echo \"example.com\" | python3 Domain-Hijacking.py")
    else:
        domains: List[str] = stdin.read().strip().split("\n")
        for domain in domains:
            try:
                answers = resolve(domain, "CNAME")      
                cname: str = answers[0].to_text()
                if NXDomain(domain):
                    print(f"[{colored('NXDOMAIN', 'green')}] {colored(domain, 'yellow')} [{colored(cname, 'blue')}]")
            except KeyboardInterrupt:
                break
            except:
                continue
