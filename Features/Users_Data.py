import mysql.connector
from mysql.connector import Error
from RandomDetails import Generate_id
from Date_Time import Current_datetime



def Insret_UserData(userid, username, userpassword, userrole, insertedat):
    Es_Connect = None
    Es_Curosor = None

    try:
        Es_Connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vishal@123",
            database="Test_selenium",
            # auth_plugin="mysql_native_password"  # Specify the auth plugin
        )
        if Es_Connect.is_connected():
            Es_Curosor = Es_Connect.cursor()

            # Insert the data into the database
            Insert_query = "INSERT INTO User_Details(id, user_name, user_password, user_role, inserted_at) VALUES(%s, %s, %s, %s, %s)"
            data = (userid, username, userpassword, userrole, insertedat)
            Es_Curosor.execute(Insert_query, data)

            # Commit the transaction
            Es_Connect.commit()
            print("User data inserted successfully.")

    except Error as e:
        print(f"Error occurred: {e}")

    finally:
        # Close cursor if it was successfully created
        if Es_Curosor:
            Es_Curosor.close()

        # Close the connection
        if Es_Connect and Es_Connect.is_connected():
            Es_Connect.close()
            print("MySQL connection closed.")

# Call the function

unique_id = Generate_id()
current_time = Current_datetime()

Insret_UserData(unique_id, "Superadmin", "Test@12345", "SUPERADMIN", current_time)
