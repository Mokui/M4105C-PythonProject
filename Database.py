import sqlite3

if __name__ == '__main__':
    main()

def main():
    database = "database.db"
    
    bddInstall = """CREATE TABLE IF NOT EXIST installation_table(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        adress VARCHAR(255),
        postalcode VARCHAR,
        city VARCHAR,
        latitude DECIMAL,
        longitude DECIMAL);
          """
    
    #create a database collection
    conn = create_connection(database)
    
    if conn is not None:
        # create the table
        create_table(conn, bddInstall)

    else:
        print("Error! cannot create the database connection.")
    
# Delete table
def deleteBDDInstall():
    c.execute("DROP TABLE IF EXIST installation_table")

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
    except Error as e:
        print(e)
    finally:
        conn.close()
 
    return None

# Method to create a table
def create_table(conn, create_table_sql)
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)