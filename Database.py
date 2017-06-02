import sqlite3
from jsonParser import *

def main():
    database = "database.db"

    bddInstall = """CREATE TABLE IF NOT EXISTS installation_table(
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        adress VARCHAR(255),
        postalcode VARCHAR(5),
        city VARCHAR,
        latitude DECIMAL,
        longitude DECIMAL);
          """

    bddEquip = """CREATE TABLE IF NOT EXISTS equipment_table(
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        id_install INTEGER,
        FOREIGN KEY(id_install) REFERENCES installation_table(id));
          """

    bddEquipActiv = """CREATE TABLE IF NOT EXISTS equip_activ_table(
        id_equip INTEGER,
        id_activity INTEGER,
        FOREIGN KEY(id_equip) REFERENCES equipment_table(id),
        FOREIGN KEY(id_activity) REFERENCES activity_table(id));
          """

    bddActiv = """CREATE TABLE IF NOT EXISTS activity_table(
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL);
          """

    #create a database collection
    conn = create_connection(database)

    if conn is not None:
        try:
            #delete all tables if they exists
            deleteAllBDD(conn)
        except Exception as e:
            print(e)

        # create the table
        create_table(conn, bddInstall)
        create_table(conn, bddEquip)
        create_table(conn, bddEquipActiv)
        create_table(conn, bddActiv)

    else:
        print("Error! cannot create the database connection.")

    conn.commit()
    conn.close()

# Delete table
def deleteAllBDD(conn):
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS installation_table")
    c.execute("DROP TABLE IF EXISTS equipment_table")
    c.execute("DROP TABLE IF EXISTS equip_activ_table")
    c.execute("DROP TABLE IF EXISTS activity_table")

# Delete installation table
def deleteBDDInstall():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS installation_table")

# Delete equipment table
def deleteBDDEquip():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS equipment_table")

# Delete activity table
def deleteBDDActivity():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS activity_table")

# Delete joint table
def deleteBDDEquipActiv():
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
        query = "INSERT INTO equipment_table values(?,?,?);"
        c.execute(query, (equipment.id, equipment.name, equipment.installation_id))
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
        c.execute(query, (installation.id, installation.name, installation.adress, installation.postal_code, installation.city, installation.latitude, installation.longitude))
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


def getActivity(conn, activity_id) :
    try :
        c = conn.cursor()
        query = "SELECT a.nom FROM activity_table a where a.id = ?"
        c.execute(query, activity_id)
        statement = c.fetchone()
    except Exception as e :
        print(e)

    return statement


def getEquipment(conn, equipment_id) :
    try :
        c = conn.cursor()
        query = "SELECT e.nom, e.installation FROM equipment_table e where e.id = ?"
        c.execute(query, equipment_id)
        statement = c.fetchone()
    except Exception as e :
        print(e)

    return statement


def getPosition(conn,installation_id):
    """ give the position latitude/longitude of a given installation with his ID
    :param conn: Connection object
    :param installation_id: the installation ID needed to get the latitude/longitude informations
    :return statement: Fetches the next row of a query result set, or None when no more data is available for the ID selected
    """
    try:
        c = conn.cursor()
        query = "SELECT i.latitude, i.longitude FROM installation_table i where installation_table.id == ?);"
        c.execute(query, installation_id)
        statement = c.fetchone()
    except Exception as e:
        print(e)
    return statement

def getInstallation(conn,installation_id):
    """ give the name; address; postal code; city of the given installation with his ID
    :param conn: Connection object
    :param installation_id: the installation ID needed to get the informations
    :return statement: Fetches the next row of a query result set, or None when no more data is available for the ID selected
    """
    try:
        c = conn.cursor()
        query = "SELECT i.name, i.address, i.postal_code, i.city FROM installation_table i where installation_table.id == ?);"
        c.execute(query, installation_id)
        statement = c.fetchone()
    except Exception as e:
        print(e)
    return statement

if __name__ == '__main__':
    main()
