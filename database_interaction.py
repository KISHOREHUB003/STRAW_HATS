import mysql.connector

# Define your MySQL connection parameters
config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Kamalganth@2004",
    "database": "phn",

}

def get_table_data():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    select_query = "SELECT * FROM Datasheet"
    cursor.execute(select_query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_column_data(column_name):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    select_query = f"SELECT {column_name} FROM Datasheet"
    cursor.execute(select_query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def add_data(name, phone, address):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    insert_query = "INSERT INTO Datasheet (Name_, Phone, Address) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, phone, address))
    connection.commit()
    cursor.close()
    connection.close()

def edit_data(name, column_name, new_value):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    update_query = f"UPDATE Datasheet SET {column_name} = %s WHERE Name_ = %s"
    cursor.execute(update_query, (new_value, name))
    connection.commit()
    cursor.close()
    connection.close()

def delete_data(name):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    delete_query = "DELETE FROM Datasheet WHERE Name_ = %s"
    cursor.execute(delete_query, (name,))
    connection.commit()
    cursor.close()
    connection.close()
