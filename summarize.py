import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='178.128.208.156',
                                         database='saham',
                                         user='rizkyaddon',
                                         password='Jakarta123!')

    sql_select_Query = "select * from list_saham"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in saham is: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    for row in records:
        base_url_ipot = 'https://www.indopremier.com/ipotnews/newsSmartSearch.php?code='
        kode_saham = row[1] + ""
        netval_current =  str(row[16])
        netval_1day_ago = str(row[16])
        netval_2day_ago = str(row[20])
        netval_3day_ago = str(row[21])
        netval_4day_ago = str(row[22])
        netval_5day_ago = str(row[23])
        full_url = base_url_ipot + kode_saham
        print("Id = ", row[0], )
        print("Kode Saham = ", row[1])
        print("Nama Saham  = ", row[2])
        sql = "UPDATE list_saham SET netval_1day_ago = "+netval_1day_ago+", netval_2day_ago = "+netval_2day_ago+", netval_3day_ago = "+netval_3day_ago+", netval_4day_ago = "+netval_4day_ago+",  netval_5day_ago = "+netval_5day_ago+" WHERE kode_saham = '"+ kode_saham +"'"

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