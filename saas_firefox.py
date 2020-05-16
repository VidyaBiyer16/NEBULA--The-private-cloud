#!/usr/bin/python36


print("content-type:text/html")
print("\n")

import subprocess
import os
import cgi


print("hello i am working")

file3=open("/var/www/cgi-bin/saas_firefox.yml","w")
file3.write("""- hosts: all
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
        src: "/root/firefox_saas.tar"
        dest: "/root/firefox_saas.tar"


    - docker_image:
        name: "firefox:v5"
        load_path: "/root/firefox_saas.tar"
        state: present

    - docker_container:
        name: d1
        image: firefox:v5
        volumes:
          - /run/media/root/RHEL-7.5\ Server.x86_64:/dvd
          - /root/rhel7rpm:/extras
          - /tmp/.X11-unix/:/tmp/.X11-unix/
        state: started
        command: firefox
""")

file3.close()
print("yml file ready")

x = subprocess.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/saas_firefox.yml")
print(x)
print("<h3> FIREFOX has been launched on your system </h3>")
print("<h4> THANK YOU</h4>")                                                  
