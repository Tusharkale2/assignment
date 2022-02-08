import mysql.connector as sqlcon
db=sqlcon.connect(host='localhost',user='root',passwd='',database='carrental')
cur=db.cursor()
cur.execute('update tblusers set City="Mumbai" where id=3')
cur.execute('select FullName,EmailId,City from tblusers')
for i in cur :
    print(i)
cur.close()
