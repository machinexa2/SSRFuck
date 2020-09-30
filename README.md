# SSRFuck
## Description
Inspiried by `jsfuck` and `brainfuck`, two words which have no relation with my tool. Test for SSRF against a list of URLs

## Features
1. Threaded testing of SSRF against a list of URLs.
2. Use of faster_than_requests for fastness!
3. Three input modes to be used with other tool!

## Usage
```
usage: SSRFucker [-h] [-w WORDLIST] [-d DOMAIN] [-s SERVER] [-t THREADS] [-b]

Simple tool for SSRF

optional arguments:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Absolute path to wordlist
  -d DOMAIN, --domain DOMAIN
                        Domain name
  -s SERVER, --server SERVER
                        Server name
  -t THREADS, --threads THREADS
                        Number of threads
  -b, --banner          Print banner and exit

Check your server logs
```

## Example
1. General SSRF (using wordlist)
* ```SSRFuck -w hakrawler.data -t 100 -s SERVERNAME```  
2. General SSRF (using url)
* ```SSRFuck -u http://localhost:80/?file=page.html -s SERVERNAME```
3. General SSRF (using stdin)
* ```echo "uber.com" | hakrawler -plain -depth 5 | SSRFuck --- -t 100 -s SERVERNAME```

## Caveats
1. None i guess.
