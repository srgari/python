#### 
## SQLite, manolo!
# Tô aprendendo!

# Parte 1: Básico - criar conexão
# Parte 2: Básico - criar tabelas

############################################################################
### PARTE 1: CRIAR CONEXÃO ###
#%%
import sqlite3
from sqlite3 import Error 

# First, we define a function that connects to an SQLite database
# specified by the database file
###
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)

    except Error as e:
        print(e)
    
    finally:
        if conn:
            conn.close()

#%%
    if __name__ == '__main__':
        ### create connection to a file
        create_connection('pythonsqlite.db')
        ### create connection to RAM 
        # create_connection(':memory:')

# %%
### PARTE 2: CRIAR TABELA

def create_connection(db_file):
    """ create a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: connection object or None
    """

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print(e)

    return conn

# %%
def create_table(conn, create_table_sql):
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

def main():
    database = r"pythonsqlite.db"

    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMARY KEY,
        name text NOT NULL,
        begin_date text,
        end_date text
    );"""

    conn = create_connection(database)
    if conn:
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection")    
main()

# %%
