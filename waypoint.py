from unixTime import UnixTime
class Waypoint():
    def __init__(self,*args) -> None:
        self.time:int=UnixTime(int(args[0]))
        self.latitude:float=args[1]
        self.longitude:float=args[2]
        self.baro_altitude:float=args[3]
        self.true_track:float=args[4]
        self.on_ground:bool=args[5]

        pass
    def __str__(self) -> str:
        return f"Time:{self.time} Lat:{self.latitude} Long:{self.longitude} Alt:{self.baro_altitude}"