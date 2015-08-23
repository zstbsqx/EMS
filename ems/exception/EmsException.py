
class EmsException(Exception):
    def __init__(self, code, desc):
        self.code = code
        self.desc = desc
