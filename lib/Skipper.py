from lib.PathFunctions import PathFunction

class Skip:
    def __init__(self):
        self.PathFunctions = PathFunction()
        self.path_list = []
        self.netloc_list = []
        self.parameter_list = {}
        self.uparameter_list = {}

    def add_netloc(self, netloc: str) -> bool:
        if self.check_netloc(netloc):
            return False
        self.netloc_list.append(netloc)
        return True

    def add_path(self, path: str) -> bool:
        if self.check_path(path):
            return False
        self.path_list.append(path)
        return True

    def add_parameter(self, url: str, parameter_list: list) -> list:
        url = self.PathFunctions.ender(url, '?')
        if bool(self.parameter_list.get(url)):
            var = self.parameter_list[url]
            var.update(set(parameter_list))
            self.parameter_list[url] = var
            return False
        self.parameter_list[url] = set(parameter_list)
        return True

    def check_netloc(self, netloc: str) -> bool:
        return bool(netloc in self.netloc_list)

    def check_path(self, path: str) -> bool:
        return bool(path in self.path_list)

    def check_parameter(self, url: str, parameter: str) -> bool:
        url = self.PathFunctions.ender(url, '?')
        exist = bool(self.parameter_list.get(url))
        if exist:
            for self_parameter in self.parameter_list[url]:
                if self_parameter == parameter:
                    return True
        return False

    def add_unique_parameter(self, parameter_list: list) -> bool:
        for parameter in parameter_list:
            if not parameter in self.uparameter_list:
                self.uparameter_list[parameter] = 0
            else:
                self.uparameter_list[parameter] += 1
        return True

    def check_unique_parameter(self, parameter: str):
        if not parameter in self.uparameter_list:
            return False
        if self.uparameter_list[parameter] >= 75:
            return False
        return True
