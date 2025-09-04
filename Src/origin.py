class Origin:
    def __init__(self, name):
        self.name = name
    
    def toDict(self):
        return {"name": self.name}
    
    @classmethod
    def fromDict(cls, data):
        return cls(data["name"])