from termcolor import colored

from lib.Globals import ColorObj

def banner():
    from pyfiglet import print_figlet
    print_figlet('SSRFuck', font='larry3d', colors='BLUE')
    print(colored('A SSRF Finding tool!', color='red', attrs=['bold']))
    print(colored('Use SSRF payload everywhere!', color='red', attrs=['bold']))

def starter(argv):
    if argv.banner:
        banner()
        exit(0)
    if not argv.wordlist:
        if not argv.url:
            print("{} Use --help".format(ColorObj.bad))
            exit()
        else:
            return [argv.url.rstrip(' ')]
    else:
        return [line.rstrip('\n') for line in open(argv.wordlist)]
