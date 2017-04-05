import sqlite3

def main():
    database = "database.db"

    bddInstall = """CREATE TABLE IF NOT EXISTS installation_table(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        adress VARCHAR(255),
        postalcode VARCHAR,
        city VARCHAR,
        latitude DECIMAL,
        longitude DECIMAL);
          """

    bddEquip = """CREATE TABLE IF NOT EXISTS equipement_table(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        id_install INTEGER,
        FOREIGN KEY(id_install) REFERENCES installation_table(id));
          """

    bddEquipActiv = """CREATE TABLE IF NOT EXISTS equip_activ_table(
        id_equip INTEGER,
        id_activity INTEGER,
        FOREIGN KEY(id_equip) REFERENCES equipement_table(id),
        FOREIGN KEY(id_activity) REFERENCES activity_table(id));
          """

    bddActiv = """CREATE TABLE IF NOT EXISTS activity_table(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL);
          """

    #create a database collection
    conn = create_connection(database)

    if conn is not None:
        try:
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
    c.execute("DROP TABLE IF EXISTS equipement_table")
    c.execute("DROP TABLE IF EXISTS equip_activ_table")
    c.execute("DROP TABLE IF EXISTS activity_table")

# Delete installation table
def deleteBDDInstall():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS installation_table")

# Delete equipment table
def deleteBDDEquip():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS equipement_table")

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

if __name__ == '__main__':
    main()
