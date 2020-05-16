#!/usr/bin/python36

print("content-type:text/html")
print("\n")

import subprocess
import os
import cgi


file1=open("/var/www/cgi-bin/jupyter.yml", "w")
file1.write("""- hosts: all
  tasks:

   - yum:
       name: docker-ce
       state: present

   - copy:
       src: "/root/get-pip.py"
       dest: "/root/get-pip.py"

   - command: "python get-pip.py"

   - pip:
       name: docker
       state: latest


   - service:
       name: docker
       state: started

   - copy:
       src: "/root/jupyter_saas.tar"
       dest: "/root/jupyter_saas.tar"

   - docker_image:
       name: "jupyter:v3"
       load_path: "/root/jupyter_saas.tar"
       state: present

   - docker_container:
       name: "j1"
       image: "jupyter:v3"
       state: started
       interactive: true
       ipc_mode: host
       tty: true
       exposed_ports: 8888
       published_ports: "2400:8888"
       command: "jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root"
""")

file1.close()

subprocess.getoutput("ansible-playbook /var/www/cgi-bin/jupyter.yml")


print("<h2>Jupyter Notebook has successfully been launched on your system</h2>")
print("\n")
print("<h3>Jupyter notebook can be accessed by typing localhost:2400 in your browser</h3>")
print("\n")
print("please do save your work before exiting the notebook") 	
print("<h3>THANK YOU</h3>")



