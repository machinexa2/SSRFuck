# SSRFuck
## Description
Inspiried by `jsfuck` and `brainfuck`, two words which have no relation with my tool. Mass hunt for SSRF against a list of URLs or a single url.

## Features
1. Mass testing of SSRF against a list of URLs.
2. Use of HTTP headers for SSRF.
3. Automatic creation of public url when provided blind SSRF program path.

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
1. SSRF (using wordlist)
* ```SSRFuck -w hakrawler.data -t 100 -s SERVERNAME```  
2. SSRF (using url)
* ```SSRFuck -u http://localhost:80/?file=page.html -s SERVERNAME```
3. SSRF (using stdin)
* ```echo "uber.com" | hakrawler -plain -depth 5 | SSRFuck --- -t 100 -s SERVERNAME```
4. SSRF without a server name (serverless hosting)
* ```SSRFuck -u http://google.com/?q=hello+world -a /var/www/html/B-XSSRF/,request.php```  
If index.php acts as request.php, then `,request.php` is optional!

## Note
* Download from releases as they are more stable and if you want to become beta tester, use directly SSRFUCK.py and raise issue
* Venv isn't necessary in all of my tools, works with latest version of all depedencies, if it doesn't feel free to raise issue
