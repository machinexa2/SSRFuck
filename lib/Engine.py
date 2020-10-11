from termcolor import colored
from urllib.parse import urlparse
from faster_than_requests import get, head

from lib.Globals import ColorObj
from lib.ParamReplacer import ParamReplace

class Engine:
    def __init__(self):
        self.Replacer = ParamReplace()

    def generate_payloads(self, URLs: list, replace_string: str) -> tuple:
        payloads_url = []
        for URL in URLs:   
            print(f"{ColorObj.information} Generating payload for: {colored(URL, color='cyan')}")
            half_payload = urlparse(URL)
            if half_payload.query:
                parameter, value = self.Replacer.expand_parameter(half_payload.query)
                replacer_list = self.Replacer.replacement(parameter, value, replace_string)
                full_payload = self.Replacer.generate_url('http://' + half_payload.netloc + half_payload.path, replacer_list)
                payloads_url.append(full_payload)
        return payloads_url
 
    def try_payload(self, URL: str) -> bool:
        print(f"{ColorObj.good} Trying to send request! {colored(URL, color='cyan')}")
        try:
                get(URL, timeout=5000)
                head(URL, timeout=5000)
        except Exception as E:
            print(E.__class__)
