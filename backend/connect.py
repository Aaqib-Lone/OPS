import psycopg2

#establishing the connection

def connection_to_db(data):
    conn = psycopg2.connect(
    database="ops", user='postgres', password='root', host='localhost', port= '5432'
    )
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    cursor.execute(data)
    conn.commit()
    conn.close()
    cursor.close()
    return data

def fetch_from_db(data):
    # conn = psycopg2.connect(
    # database="ops", user='postgres', password='root', host='localhost', port= '5432'
    # )
    # #Creating a cursor object using the cursor() method
    # cursor = conn.cursor()
    # #Executing an MYSQL function using the execute() method
    # cursor.execute(data)
    # conn.commit()
    # # cursor.execute(f"select * from register")
    # # Fetch a single row using fetchone() method.
    # data = cursor.fetchone()
    # print("data: ",data)
    # (id,) = data  # Unpacking the tuple into the variable 'id'
    # print(id)
    # #Closing the connection
    # conn.close()
    # cursor.close()
    # return id
    conn = psycopg2.connect(
        database="ops", user='postgres', password='root', host='localhost', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute(data)
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return data[0] if data else None