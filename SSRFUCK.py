#!/usr/bin/python3
from termcolor import colored
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor 

from lib.SSRFuck import SSRFuck
from lib.Functions import starter
from lib.PathFunctions import PathFunction

parser = ArgumentParser(description=colored("Simple tool for SSRF", color='yellow'), epilog=colored("Check your server logs", color='yellow'))
input_group = parser.add_mutually_exclusive_group()
input_group.add_argument("---", "---", dest="stdin", help="Stdin")
input_group.add_argument("-w", "--wordlist", type=str, help="Absolute path to wordlist")
input_group.add_argument("-u", "--url", type=str, help="Url to try")
parser.add_argument("-s", "--server", type=str, help="Server name(Burp Collaborator/Ngrok)")
parser.add_argument("-t", "--threads", type=int, help="Number of threads")
parser.add_argument("-b", "--banner", action="store_true", help="Print banner and exit")
argv = parser.parse_args()

input_wordlist = starter(argv)
FPathApp = PathFunction()
ssrfuck_object = SSRFuck()

def main():
    payloads_list = ssrfuck_object.generate_payloads(input_wordlist, FPathApp.urler(argv.server))
    the_payloads = [payload for payload_list in payloads_list for payload in payload_list]
    del payloads_list
    with ThreadPoolExecutor(max_workers=argv.threads) as submitter:
        futures_objects = [submitter.submit(ssrfuck_object.try_payload, triable) for triable in the_payloads]
    print(f"{ColorObject.good} Success. Check your server logs for bounty!")

if __name__ == "__main__":
    main()
