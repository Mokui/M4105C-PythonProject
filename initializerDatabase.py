from json_parser import *
from Database import *

def main():
    # get a connection to send requests to the database
    conn = create_connection("database.db")

    # parsing json files
    list_activities, list_equip_activ = parse_activities()
    list_equipments = parse_equipments()
    list_installations = parse_installations()

    # insert each object in the database
    
    for activity in list_activities:
        insert_activity(conn, activity)

    for equip_activ in list_equip_activ:
        insert_equip_activ(conn, equip_activ)

    for equipment in list_equipments:
        insert_equipment(conn, equipment)

    for install in list_installations:
        insert_installation(conn, install)

    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    main()
