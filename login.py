#!/usr/bin/python36

#print("content-type:text/html")
#print("\n")

import cgi
import subprocess
import pymysql

pymysql.install_as_MySQLdb()

import MySQLdb


if __name__ == '__main__':
   db = MySQLdb.connect("localhost","root","XXXX","project" )
   cursor = db.cursor()
   form = cgi.FieldStorage()
   un = form.getvalue('username')
   passwd = form.getvalue('password')
   sql1 = "select usn,password from student where usn='"+un+"' and password='"+passwd+"'"
   sql2 = "insert into login values('"+un+"' , NOW())"
   sql3 = "select tid,password from teacher where tid='"+un+"' and password='"+passwd+"'"
   if(cursor.execute(sql1)):
      cursor.execute(sql2)
      db.commit()
      print("content-type:text/html")
      print("Location: http://192.168.43.72/MAIN.html?usn=%s" %un)
      print("\n")

      print('<html>')
      print('<head>')
      print('<meta http-equiv="refresh" content="0;url= MAIN.html?usn=%s" />' %un) 
      print('</head>')
      print('</html>')

   elif(cursor.execute(sql3)):
      cursor.execute(sql2)
      db.commit()
      print("content-type:text/html")
      print("Location: http://192.168.43.72/MAIN_TEACHER.html?usn=%s" %un)
      print("\n")

      print('<html>')
      print('<head>')
      print('<meta http-equiv="refresh" content="0;url= MAIN_TEACHER.html?usn=%s" />' %un) 
      print('</head>')
      print('</html>')

   else:
      print("content-type:text/html")
      print("Location: http://192.168.43.72/cloudlogin2.html")
      print("\n")

      print('<html>')
      print('<head>')
      print('<meta http-equiv="refresh" content="0;url= cloudlogin2.html" />') 
      print('</head>')
      print('</html>')

