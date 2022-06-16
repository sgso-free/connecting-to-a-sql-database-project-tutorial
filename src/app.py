
#USE POSTGRES

import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

#load env file, configuration file
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

conn = psycopg2.connect(database= os.getenv('DB_NAME'),
                        user = os.getenv('DB_USER'),
                        password= os.getenv('DB_PASSWORD'),
                        host = os.getenv('DB_HOST'),
                        port = os.getenv('DB_PORT'))
 

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

#Manual option
"""
cursor = conn.cursor()
cursor.execute("CREATE TABLE publishers(publisher_id INT NOT NULL,name VARCHAR(255) NOT NULL, PRIMARY KEY(publisher_id));")
cursor.execute("CREATE TABLE authors(author_id INT NOT NULL,first_name VARCHAR(100) NOT NULL, middle_name VARCHAR(50) NULL, last_name VARCHAR(100) NULL, PRIMARY KEY(author_id));")
cursor.execute(CREATE TABLE books(book_id INT NOT NULL,title VARCHAR(255) NOT NULL, total_pages INT NULL, rating DECIMAL(4, 2) NULL,  isbn VARCHAR(13) NULL, published_date DATE, publisher_id INT NULL,PRIMARY KEY(book_id), CONSTRAINT fk_publisher FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id));")

conn.commit()


conn.close()
"""

#File option
def executeFromFile(engine,file_name):
    sql_file=open(f'src/sql/{file_name}','r')
    content_sql=sql_file.read()
    sql_file.close()
    allStatements=content_sql.split(';')
    for statement in allStatements:
        try:
            engine.execute(statement)
        except Exception as e:
            print("Not execute this comand:",e)

cursor = conn.cursor() 
#Create table
#executeFromFile(cursor,"create.sql")  
#Insert data
#executeFromFile(cursor,"insert.sql")
#Drop the table from schema
#executeFromFile(cursor,"drop.sql")
#conn.commit()
 

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

"""
cursor = conn.cursor()
cursor.execute("INSERT INTO Movies(id,title,rating) VALUES ('3','Toy Story 3',3), ('4','Harry Potters 1',5);")
conn.commit()
conn.close()
"""

"""
with self.connection as cursor:
    cursor.execute(open("sql/insert.sql", "r").read())
conn.commit() 
"""
# 4) Use pandas to print one of the tables as dataframes using read_sql function

"""
cursor = conn.cursor()
df = pd.read_sql('SELECT * FROM Movies', conn)
conn.close()

print(df)
"""
 
cursor = conn.cursor()
df = pd.read_sql('SELECT * FROM books', conn)
conn.close()

print(df) 
