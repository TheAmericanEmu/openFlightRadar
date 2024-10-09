import requests

class Aircaft():
    def __init__(self,**kwargs):
        self.icao24 = kwargs[0]
        self.callsign = kwargs[1]
        self.origin_country = kwargs[2]
        self.time_position = kwargs[3]
        self.last_contact = kwargs[4]
        self.longitude=kwargs[5]
        self.latitude=kwargs[6]
        self.baro_altiude=kwargs[7]
        self.on_ground=kwargs[8]
        self.velocity=kwargs[9]
        self.true_track=kwargs[10]
        self.vertical_rate=kwargs[11]
        self.sensors=kwargs[12]
        self.geo_altitude=kwargs[13]
        self.squak=kwargs[14]
        self.spi=kwargs[15]
        self.position_source=self.prase_position_source(kwargs[16])
        self.category=self.prase_category(kwargs[17])
        pass
    def prase_position_source(self,num:int)-> str:
        if(num==0):
            return "ADS-B"
        elif(num==1):
            return "ASTERIX"
        elif(num==2):
            return "MLAT"
        else:
            return "FLARM"
    def prase_category(self,num:int)-> str:
        if(num==0):
            return "No information at all"
        elif(num==1):
            return "No ADS-B Emitter Category Information"
        elif(num==2):
            return "Light"
        elif(num==3):
            return "Small"
        elif(num==4):
            return "Large"
        elif(num==5):
            return "High Vortex Large" ##ex/ B-757
        elif(num==6):
            return "Heavy"
        elif(num==7):
            return "High Performance"
        elif(num==8):
            return "Rotorcraft"
        elif(num==9):
            return "Glider / sailplane"
        elif(num==10):
            return "Lighter-than-air"
        elif(num==11):
            return "Parachutist / Skydiver"
        elif(num==12):
            return "Ultralight / hang-glider / paraglider"
        elif(num==13):
            return "Reserved"
        elif(num==14):
            return "Unmanned Aerial Vehicle"
        elif(num==15):
            return "Space / Trans-atmospheric vehicle"
        elif(num==16):
            return "Surface Vehicle – Emergency Vehicle"
        elif(num==17):
            return "Surface Vehicle – Service Vehicle"
        elif(num==18):
            return "Point Obstacle (includes tethered balloons)"
        elif(num==19):
            return "Cluster Obstacle"
        elif(num==20):
            return "Line Obstacle"
    def __str__(self):
        return f"{self.callsign} is a of class {self.category} travling at {self.velocity} at {self.baro_altiude} at {self.latitude}* {self.longitude}* degrees"
    

    if __name__=="__main__":
        all_flights = requests.get('https://opensky-network.org/api/states/all').json
        print(all_flights)