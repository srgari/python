#%%
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
###########################################################################
### PARTE 2: CRIAR TABELA
#1. Conexão à base: Criar conn - sqlite3.connect()
#2. "porteiro": Cursor: conn.cursor()
#3. criar tabela: Cursor.execute()

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
        Cursor = conn.cursor()
        Cursor.execute(create_table_sql)
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

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks(
        id intenger PRIMARY KEY,
        name text NOT NULL,
        priority integer,
        status_id integer NOT NULL,
        project_id integer NOT NULL,
        begin_date text NOT NULL,
        end_date text NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    );"""

    conn = create_connection(database)
    if conn:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection")    
main()

# %%
############################################################################
### PARTE 3: ADICIONAR VALORES NA TABELA
#- Conexão à base: conn = sqlite3.connect()
#- Cursor: Cursor = conn.cursor()
#- Inserir dados: Cursor.execute() 

#  If you want to pass arguments to the INSERT statement, 
# you use the question mark (?) as the placeholder for each argument

### create connection:
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn


### function to insert a new project into projects table
def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id    
    """
    sql = '''
    INSERT INTO projects(name, begin_date, end_date)
    VALUES(?,?,?)''' # <- check out the question marks!
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

# %%
# function to insert rows into the tasks table
def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = '''
    INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
    VALUES(?,?,?,?,?,?)''' # <- check out the place holders!
    
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

# %%
# main function: runs the functions above
def main():
    database = 'pythonsqlite.db'

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('Cool App with SQLite & Python','2015-01-01','2015-01-30')
        project_id = create_project(conn, project)

        # tasks
        task_1 = ('analyse the requirements of the app',1,1, project_id, '2015-01-01','2015-01-02')
        task_2 = ('confirm with user about the top requirements',1,1, project_id, '2015-01-03','2015-01-05')

        create_task(conn, task_1)
        create_task(conn, task_2)

main()
# %%
import pandas as pd 
help(pd.read_sql)
conn = sqlite3.connect('pythonsqlite.db')
pd.read_sql(sql = 'SELECT name FROM sqlite_master', con = conn)
# %%
