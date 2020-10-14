class ParamReplace:
    def __init__(self):
        pass
    
    def replacement(self, parameter: list, value: list, replace_str: str) -> list:
        small_counter  = []
        parameter_list = []
        parameter_length = len(parameter)
        counter = 0
        while counter != parameter_length:
            temp = value[counter]
            for i in range(parameter_length):
                value[counter] = replace_str
                small_counter.append(parameter[i] + '=' + value[i])
            parameter_list.append(small_counter)
            value[counter] = temp
            counter += 1
            small_counter = []
        return parameter_list

    def generate_url(self, half_url: str, replaced_parameter: list) -> list:
        url_var = []
        for each in replaced_parameter:
            if half_url[-1] != "?":
                url_var.append(half_url + '?' + str("&".join(each)))
            else:
                url_var.append(half_url + str("&".join(each)))
        return url_var

    def expand_parameter(self, query_data: str) -> tuple:
        from re import findall
        p,q = [],[]
        for parameters,values in findall(r'([^&]+)=([^&]+)', query_data):
            p.append(parameters)
            q.append(values)
        if len(p) != len(q):
            return False,False
        else:
            return p,q

    def auto(self, upto_path_url, parsed_query, replace_str):
        apath, bpath = self.expand_parameter(parsed_query)
        xpath = self.replacement(apath, bpath, replace_str)
        ypath = self.generate_url(upto_path_url, xpath)
        return ypath
