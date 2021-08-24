

class SearchProvider (object):
    def __init__(self, name):
        print("init")
        self.name = name
    
    

class IpapiSearch (SearchProvider):
    def __init__(self):
        super().__init__("ipapi")
