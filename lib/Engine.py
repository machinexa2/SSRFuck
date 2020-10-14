from urllib.parse import urlparse
from lib.ParamReplacer import ParamReplace

class Engine:
    def __init__(self):
        self.Replacer = ParamReplace()

    def generate_payloads(self, urls: list, replace_string: str) -> tuple:
        p = []
        for f in filter(lambda x: x.query != "", map(urlparse, urls)):
            p.append(self.Replacer.auto('http://' + f.netloc + f.path, f.query, replace_string)[0])
        return p
