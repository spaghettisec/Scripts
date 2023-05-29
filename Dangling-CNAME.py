#!/usr/bin/python3
from typing import List
from sys import argv, stdin
from termcolor import colored
from socket import gethostbyname
from dns.resolver import resolve, query

def nxdomain(domain: str) -> bool:
    try:
        query(domain)
        return False
    except:
        return True


if __name__ == '__main__':
    if stdin.isatty():
        print("echo \"example.com\" | python3 Dangling-CNAME.py")
    else:
        domains: List[str] = stdin.read().strip().split("\n")
        for domain in domains:
            try:
                answers =  resolve(domain, "CNAME")      
                cname: str = answers[0].to_text()
                if len(cname) > 0 and nxdomain(domain):
                    print(f"[{colored('Dangling CNAME', 'green')}] {colored(domain, 'yellow')} [{colored(cname, 'blue')}]")
            except KeyboardInterrupt:
                break
            except:
                continue
