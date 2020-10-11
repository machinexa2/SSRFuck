from termcolor import colored

from lib.Globals import ColorObj

def banner():
    banner = '\x1b[5m\x1b[1m\x1b[40m\x1b[31m   __________ ____  ______           __  \n  / ___/ ___// __ \\/ ____/_  _______/ /__\n  \\__ \\\\__ \\/ /_/ / /_  / / / / ___/ //_/\n ___/ /__/ / _, _/ __/ / /_/ / /__/ ,<   \n/____/____/_/ |_/_/    \\__,_/\\___/_/|_|  \n                                         \n\x1b[0m'
    print(banner)
    print(colored('Let"s hunt for SSRF!', color='red', attrs=['bold']))

def starter(argv):
    from sys import stdin
    if argv.banner:
        banner()
        exit(0)
    if not argv.server and not argv.auto:
        print(f"{ColorObj.bad} Use --help")
        exit()
    if not argv.wordlist:
        if not argv.url:
            if not argv.stdin:
                print("{ColorObj.bad} Use --help")
            else:
                return [i.strip(' ') for i in stdin.read().split('\n') if i]
        else:
            return [argv.url.rstrip(' ')]
    else:
        return [line.rstrip('\n') for line in open(argv.wordlist)]
