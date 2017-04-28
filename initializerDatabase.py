from jsonParser import *
from Database import *

def main():

    list_activities, list_equip_activ = parse_activities()
    list_equipments = parse_equipments()
    list_installations = parse_installations()

    for activity in list_activities:
        insert_activity(activity)

    for equip_activ in list_equip_activ:
        insert_equip_activ(equip_activ)

    for equipment in list_equipments:
        insert_equipment(equipment)

    for install in list_installations:
        insert_installation(install)

if __name__ == '__main__':
    main()
