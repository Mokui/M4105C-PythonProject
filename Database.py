import sqlite3
from json_parser import *

def main():
    """
    This method create the file database.db and create all the 4th tables we need
    """
    database = "database.db"

    bdd_install = """CREATE TABLE IF NOT EXISTS installation_table(
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        address VARCHAR(255),
        postal_code VARCHAR(5),
        city VARCHAR,
        latitude DECIMAL,
        longitude DECIMAL);
          """

    bdd_equip = """CREATE TABLE IF NOT EXISTS equipment_table(
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        familly VARCHAR,
        id_install INTEGER,
        FOREIGN KEY(id_install) REFERENCES installation_table(id));
          """

    bdd_equip_activ = """CREATE TABLE IF NOT EXISTS equip_activ_table(
        id_equip INTEGER,
        id_activity INTEGER,
        FOREIGN KEY(id_equip) REFERENCES equipment_table(id),
        FOREIGN KEY(id_activity) REFERENCES activity_table(id));
          """

    bdd_activ = """CREATE TABLE IF NOT EXISTS activity_table(
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL);
          """

    #create a database collection
    conn = create_connection(database)

    if conn is not None:
        try:
            #delete all tables if they exists
            delete_all_db(conn)
        except Exception as e:
            print(e)

        # create the table
        create_table(conn, bdd_install)
        create_table(conn, bdd_equip)
        create_table(conn, bdd_equip_activ)
        create_table(conn, bdd_activ)

    else:
        print("Error! cannot create the database connection.")

    conn.commit()
    conn.close()

# Delete table
def delete_all_db(conn):
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS installation_table")
    c.execute("DROP TABLE IF EXISTS equipment_table")
    c.execute("DROP TABLE IF EXISTS equip_activ_table")
    c.execute("DROP TABLE IF EXISTS activity_table")

# Delete installation table
def delete_table_install():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS installation_table")

# Delete equipment table
def delete_table_equip():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS equipment_table")

# Delete activity table
def delete_table_activity():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS activity_table")

# Delete joint table
def delete_table_equip_activ():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS equip_activ_table")

# Create a connection to the database
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Exception as e:
        print(e)

    return None

# Method to create a table
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

# Method to insert a row in Activity
def insert_activity(conn, activity):
    """ insert a row of Activity in database
    :param conn: Connection object
    :param activity: the activity needed to INSERT into the database
    :return:
    """
    try:
        c = conn.cursor()
        query = "INSERT INTO activity_table VALUES(?, ?);"
        c.execute(query,(activity.id, activity.name))
    except Exception as e :
        print(e)

# Method to insert a row in Equipment
def insert_equipment(conn, equipment):
    """ insert a row of Equipment in database
    :param conn: Connection object
    :param equipment: the equipment needed to INSERT into the database
    :return:
    """
    try:
        c = conn.cursor()
        query = "INSERT INTO equipment_table values(?,?,?,?);"
        c.execute(query, (equipment.id, equipment.name, equipment.familly, equipment.installation_id))
    except Exception as e:
        print(e)

# Method to insert a row in Installation
def insert_installation(conn,installation):
    """ insert a row of Installation in database
    :param conn: Connection object
    :param installation: the installation needed to INSERT into the database
    :return:
    """
    try:
        c = conn.cursor()
        query = "INSERT INTO installation_table VALUES(?, ?, ?, ?, ?, ?, ?);"
        c.execute(query, (installation.id, installation.name, installation.address, installation.postal_code, installation.city, installation.latitude, installation.longitude))
    except Exception as e :
        print(e)

# Method to insert a row in EquipActiv
def insert_equip_activ(conn,equip_activ):
    """ insert a row of EquipActiv in database
    :param conn: Connection object
    :param equip_activ: the equip_activ needed to INSERT into the database
    :return:
    """
    try:
        c = conn.cursor()
        query = "INSERT INTO equip_activ_table values(?,?);"
        c.execute(query, (equip_activ.activity_id, equip_activ.equipment_id))
    except Exception as e:
        print(e)

def get_activity(conn, activity_id) :
    """
    Give the activity matched with the given id
    :param conn: Connection object
    :param activity_id: the activity ID needed to get the information
    :return activity: the Activity object if matched, None if not
    """
    try :
        activity = None
        c = conn.cursor()
        query = "SELECT a.name FROM activity_table a where a.id = ?"
        c.execute(query, (activity_id, ))
        statement = c.fetchone()
        if statement != None :
            activity = Activity(activity_id, statement[1])
    except Exception as e :
        print(e)

    return activity

def get_activities_by_equipment_and_name(conn, equipment_id, name) :
    """
    Give a list of activities that matched with the given equipment_id
    and a part of the activity name.
    :param conn: Connection object
    :param equipment_id: the equipment ID needed to get the information
    :param name: A part of the activity's name searched
    :return activity: a list of Activity object if matched, an empty list if not
    """
    activities = []
    name = "%" + name + "%"
    try :
        c = conn.cursor()
        query = "SELECT a.id, a.name FROM activity_table a, equip_activ_table ea where ea.id_equip = ? and a.id = ea.id_activity and a.name LIKE ?"
        c.execute(query, (equipment_id, name, ))
        statement = c.fetchall()

        for obj in statement :
        	activities.append(Activity(obj[0], obj[1]))

    except Exception as e :
        print(e)

    return activities


def get_equipment(conn, equipment_id) :
    """
    Give the equipment matched with the given id
    :param conn: Connection object
    :param equipment_id: the equipment ID needed to get the information
    :return equipment: the Equipment object if matched, None if not
    """
    try :
        equipment = None
        c = conn.cursor()
        query = "SELECT e.nom, e.familly, e.installation  FROM equipment_table e where e.id = ?"
        c.execute(query, (equipment_id, ))
        statement = c.fetchone()

        if statement != None :
            equipment = Equipment(equipment_id, statement[0], statement[1], statement[2])
    except Exception as e :
        print(e)

    return equipment


def get_equipments_by_installation(conn, installation_id):
    """ give all the Equipment objects that have this installation_id 
    :param conn: Connection object
    :param installation_id: the installation ID needed to get the informations
    :return equipments: a list of Equipment object if matched, an empty list if not
    """
    try:
        statement = None
        c = conn.cursor()
        query = "SELECT e.id, e.name, e.familly FROM equipment_table e where e.id_install == ? and 1 = 1 order by e.id"
        c.execute(query, (installation_id,))
        statement = c.fetchall()

        equipments = []
        for obj in statement :
            equipments.append(Equipment(obj[0], obj[1], obj[2], installation_id))
    except Exception as e:
        print(e)

    return equipments


def get_position(conn,installation_id):
    """ give the position latitude/longitude of a given installation with his ID
    :param conn: Connection object
    :param installation_id: the installation ID needed to get the latitude/longitude informations
    :return position: a list of two floating numbers if found, an empty list if not
    """
    try:
        position = []
        c = conn.cursor()
        query = "SELECT i.latitude, i.longitude FROM installation_table i where installation_table.id == ?);"
        c.execute(query, (installation_id, ))
        statement = c.fetchone()

        if statement != None :
                position.extends(statement)
    except Exception as e:
        print(e)
    return position

def get_installation(conn,installation_id):
    """ give the name; address; postal code; city of the given installation with his ID
    :param conn: Connection object
    :param installation_id: the installation ID needed to get the informations
    :return installation: the Installation object if matched, None if not
    """
    try:
        installation = None
        c = conn.cursor()
        query = "SELECT i.name, i.address, i.postal_code, i.city, i.latitude, i.longitude FROM installation_table i where installation_table.id == ?);"
        c.execute(query, (installation_id,))
        statement = c.fetchone()

        if statement != None :
            installation = Installation(installation_id, statement[0], statement[1], statement[2], statement[3], statement[4], statement[5])
    except Exception as e:
        print(e)
    return installation

def get_installations_by_city(conn, city):
    """ give the name; address; postal code; city of the given installation with his ID
    :param conn: Connection object
    :param installation_id: the installation ID needed to get the informations
    :return installations: a list of Installation object if matched, an empty list if not
    """
    try:
        installations = []
        c = conn.cursor()
        query = "SELECT i.id, i.name, i.address, i.postal_code, i.latitude, i.longitude FROM installation_table i where i.city == ? order by i.id"
        c.execute(query, (city,))
        statement = c.fetchall()

        for obj in statement :
            installations.append(Installation(obj[0], obj[1], obj[2], obj[3], city, obj[4], obj[5]))
    except Exception as e:
        print(e)

    return installations


if __name__ == '__main__':
    main()
