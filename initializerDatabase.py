from jsonParser import *
from Database import *

def main():

    conn = create_connection("database.db")

    list_activities, list_equip_activ = parse_activities()
    list_equipments = parse_equipments()
    list_installations = parse_installations()

    for activity in list_activities:
        insert_activity(conn, activity)

    print("---1--------------------------------------------------------------------------")

    for equip_activ in list_equip_activ:
        insert_equip_activ(conn, equip_activ)
    print("---2--------------------------------------------------------------------------")

    for equipment in list_equipments:
        insert_equipment(conn, equipment)

    print("---3--------------------------------------------------------------------------")

    for install in list_installations:
        insert_installation(conn, install)

if __name__ == '__main__':
    main()
