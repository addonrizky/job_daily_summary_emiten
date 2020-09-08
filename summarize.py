import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='saham',
                                         user='root',
                                         password='Jakarta123!')

    sql_select_Query = "select * from list_saham"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in saham is: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    for row in records:
        kode_saham = row[1] + ""
    
        netval_1day_ago = str(row[16])
        netval_2day_ago = str(row[20])
        netval_3day_ago = str(row[21])
        netval_4day_ago = str(row[22])
        netval_5day_ago = str(row[23])

        foreign_netval_1dago = str(row[31])
        foreign_netval_2dago = str(row[32])
        foreign_netval_3dago = str(row[33])
        foreign_netval_4dago = str(row[34])
        foreign_netval_5dago = str(row[35])

        foreign_netval_total = float(foreign_netval_1dago) + float(foreign_netval_2dago) + float(foreign_netval_3dago) + float(foreign_netval_4dago) + float(foreign_netval_5dago)

        print("Id = ", row[0], )
        print("Kode Saham = ", row[1])
        print("Nama Saham  = ", row[2])
        sql = "UPDATE list_saham SET netval_1day_ago = "+netval_1day_ago+", netval_2day_ago = "+netval_2day_ago+", netval_3day_ago = "+netval_3day_ago+", netval_4day_ago = "+netval_4day_ago+",  netval_5day_ago = "+netval_5day_ago+", foreign_netval_1dago = "+foreign_netval_1dago+", foreign_netval_2dago = "+foreign_netval_2dago+", foreign_netval_3dago = "+foreign_netval_3dago+", foreign_netval_4dago = "+foreign_netval_4dago+", foreign_netval_5dago = "+foreign_netval_5dago+", foreign_netval_total = '"+str(foreign_netval_total)+"' WHERE kode_saham = '"+ kode_saham +"'"

        print(sql)
        cursor.execute(sql)
        connection.commit()
        #print(mycursor.rowcount, "record(s) affected")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")