#!/usr/bin/python36


print("content-type:text/html")
print("\n")

import subprocess
import os
import cgi


print("hello")
file2=open("/var/www/cgi-bin/code.yml","w")
file2.write("""- hosts: all
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
        src: "/root/codeblocks.tar"
        dest: "/root/codeblocks.tar"

    - docker_image:
        name: "codeblocks:v2"
        load_path: "/root/codeblocks.tar"
        state: present

    - docker_container:
        name: "code1"
        image: "codeblocks:v2"
        state: started
        interactive: true
        volumes:
          - /tmp/.X11-unix/:/tmp/.X11-unix/
#        env:
#          DISPLAY: "{{ lookup('env','DISPLAY')}}"
        ipc_mode: host
        tty: true

    - command: "docker exec code1 codeblocks"
      async: 6500
      poll: 10
""")

file2.close()
print("shall i run?")
x = subprocess.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/code.yml")
print(x)
print("<h2> Codeblocks has been successfully launched on your system </h2>")
print("\n")
print("please do save your work before exiting the notebook")
print("<h3>THANK YOU</h3>")




