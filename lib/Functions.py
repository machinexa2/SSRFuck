from termcolor import colored

from lib.Globals import ColorObj

def banner():
    from pyfiglet import print_figlet
    print_figlet('SSRFuck', font='larry3d', colors='BLUE')
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
