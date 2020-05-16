#!/usr/bin/python36

#print("content-type:text/html")
#print("\n")

import subprocess
import os
import cgi


form=cgi.FieldStorage()
usn=form.getvalue('usn')

present=subprocess.getoutput("ls /var/www/html/STAAS_CLOUD | grep '"+usn+"'")

if (present == usn):
    print("content-type:text/html")
    print("Location: http://192.168.43.72/STAAS_CLOUD/{0}".format(present))
    print("\n")

    print('<html>')
    print('<head>')
    print('<meta http-equiv="refresh" content="0;url= STAAS_CLOUD/{0}" />'.format(present))
    print('</head>')
    print('</html>')

else:
    print("content-type:text/html")
    print("Location: http://192.168.43.72/nodir.html?usn=%s" %usn )
    print("\n")

    print('<html>')
    print('<head>')
    print('<meta http-equiv="refresh" content="0;url=nodir.html " />')
    print('</head>')
    print('</html>')


