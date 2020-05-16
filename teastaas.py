#!/usr/bin/python36

print("content-type:text/html")
print("\n")

import subprocess 
import os
import cgi

form=cgi.FieldStorage()
size=form.getvalue('s') 
usn=form.getvalue('usn')

f5=open("/var/www/cgi-bin/tstaas.yml", "w")
f5.write("""- hosts: localhost
  tasks:
       - lvol: 
          vg: staas
          lv: {0}
          size: {1}
       - filesystem:
          fstype: ext4
          dev: /dev/staas/{0}
       - file:
          path: "/var/www/html/TEACHER_STAAS/{0}"
state: directory
          owner: apache
          mode: 0755
       - mount:
          path: "/var/www/html/TEACHER_STAAS/{0}"
          src: "/dev/staas/{0}"
          fstype: ext4
          state: mounted
       - command: "partprobe /dev/sdc"
       - lineinfile:
          path: "/etc/fstab"
          line: "/dev/staas/{0} /var/www/html/TEACHER_STAAS/{0} ext4 defaults 0 0"  
""".format(usn,size))
f5.close()
f6=open("/var/www/cgi-bin/tnfs_start.yml", "w")
f6.write("""- hosts: localhost
  tasks:
       - package:
           name: "nfs-utils"
           state: present
       - service:
           name: "nfs-utils"      
           state: started
           enabled: yes
       - copy:
           dest: "/etc/exports"      
           content: "/var/www/html/TEACHER_STAAS/{0}     *(rw,no_root_squash)"             mode: 0755
           owner: apache

   """.format(usn))
f6.close()
f7=open("/var/www/cgi-bin/tnfs_mount.yml","w")
f7.write("""- hosts: all
  tasks:
    - mount:
        fstype: nfs
        opts: defaults
        dump: 0
        passno: 0
        state: mounted
        src: 192.168.43.72:/var/www/html/TEACHER_STAAS/{0}
        path: /root/{0}
""".format(usn))
f7.close()
subprocess.getoutput("sudo ansible-playbook /var/www/cgi-bin/tstaas.yml")
subprocess.getoutput("sudo ansible-playbook /var/www/cgi-bin/tnfs_start.yml")
subprocess.getoutput("sudo ansible-playbook /var/www/cgi-bin/tnfs_mount.yml")
subprocess.getoutput("sudo mount -a")
print("YOU HAVE SUCCESSFULLY CREATE YOUR STORAGE")


