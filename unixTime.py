from datetime import datetime

class UnixTime():
    def __init__(self, UnixTimeInt:int):
        self.timeCode = UnixTimeInt
        self.readAbleTime = datetime.fromtimestamp(UnixTimeInt).strftime('%Y-%m-%d %H:%M:%S')
        pass
    def __str__(self):
        return self.readAbleTime