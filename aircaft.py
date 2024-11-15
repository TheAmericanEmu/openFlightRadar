import requests
import waypoint
import json

class Aircaft():
    def __init__(self,*args):
        #print(args)
        self.icao24 = args[0]
        self.callsign = args[1]
        self.origin_country = args[2]
        self.time_position = args[3]
        self.last_contact = args[4]
        self.longitude=args[5]
        self.latitude=args[6]
        self.baro_altiude=args[7]
        self.on_ground=args[8]
        self.velocity=args[9]
        self.true_track=args[10]
        self.vertical_rate=args[11]
        self.sensors=args[12]
        self.geo_altitude=args[13]
        self.squak=args[14]
        self.spi=args[15]
        self.position_source=self.prase_position_source(args[16])
        self.category=self.prase_category(args[16])
        self.path=self.get_path()
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
        return("NONE FOUND")

    def get_path(self)->list:
        path=requests.get(f"https://opensky-network.org/api/tracks/all?icao24={self.icao24}&time=0",auth=("TheAmericanEmu","Colin@2008"))
        if(path.status_code==200):
            path=json.loads(path.text)
            output_list=[]
            for waypoint_list in path["path"]:
                output_list.append(waypoint.Waypoint(*waypoint_list))
            return output_list
        else:
            return ["<ERROR GETTING PATH:404>"]

    
    def __str__(self):
        return f"{self.callsign} is a of class {self.category} travling at {self.velocity} at {self.baro_altiude} at {self.latitude}* {self.longitude}* degrees"
    

if __name__=="__main__":
    all_flights = requests.get('https://opensky-network.org/api/states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226',auth=("TheAmericanEmu","Colin@2008")).text
    all_flights= json.loads(all_flights)
    all_flights_list=[]
    for i in range(len(all_flights["states"])):
        aircaft_obj=Aircaft(*all_flights["states"][i])
        print(str(aircaft_obj.path[0]))
        all_flights_list.append(str()+"\n")
    with open("output.txt",encoding="UTF-8",mode="w") as file:
        file.writelines(all_flights_list)
