import json
from Activity import Activity
from Equipment import Equipment
from Installation import Installation
from EquipActiv import EquipActiv
from pprint import pprint



def parseActivities():
    """
    Parsing datas from activities.json and creating Activity and EquipActiv 
    objects from those datas
    """
    data_file = open('files/activities.json')
    datas = json.load(data_file)

    datas_list = datas["data"]
    pprint(datas_list)
    activities, equip_activties = []
    for data in datas_list :
        code = data["ActCode"]
        name = data["ActLib"]
        equip_id = data["EquipementId"]
        
        activity = Activity(code,name)
        activities.append(activity)

        equip_activity = EquipActiv(code, equip_id)
        equip_activties.append(equip_activity)

    return activities, equip_activities

def parseInstallations():
    """
    Parsing datas from installations.json and creating Installation objects
    from those datas
    """
    data_file = open('files/installations.json')
    datas = json.load(data_file)

    datas_list = datas["data"]


    installations = []
    for data in datas_list :
        #print(data["InsNoVoie"])
        code = data["InsNumeroInstall"]
        name = data["geo"]["name"]
        address =  None
        
        if data["InsNoVoie"] is not None :
            if data["InsLibelleVoie"] is not None:
                address = data["InsNoVoie"] + " " + data["InsLibelleVoie"]
        else :
            if data["InsLibelleVoie"] is not None:
                address = data["InsLibelleVoie"]
        
        postal_code = data["InsCodePostal"]
        city = data["ComLib"]
        latitude = data["_l"][1]
        longitude = data["_l"][0]

        installation = Installation(code, name, address, postal_code, city, latitude, longitude)
        installations.append(installation)

        return installations


def parseEquipments():
    """
    Parsing datas from equipments.json and creating Equipment objects
    from those datas
    """
    data_file = open('files/equipments.json')
    datas = json.load(data_file)

    datas_list = datas["data"]

    equipments = [] 

    for data in datas_list :
        
        code = data["EquipementId"]
        name = data["EquNom"]
        installation_id = data["InsNumeroInstall"]

        equipment = Equiment(code, name, installation_id, activities)
        equipment.append(equipment)

        return equipments

