#!/bin/bash

echo -n "Enter host root login: "
read host_root_login

echo -n "Enter $host_root_login password: "
read host_root_password

echo -n "Enter host ip: "
read host_ip

echo -n "Enter new password for new login (divitcfg): "
read host_password
hashed_password=$(/usr/bin/openssl passwd -6 $host_password)

cat<<EOF > inventory_add_user.txt
[new]
srv ansible_host=$host_ip
EOF

cat<<EOF > playbook_add_user.yml
---
- name: Add user for ansible
  hosts: new
  become: true
  tasks:

  - name: Добавить пользователя 'divitcfg' с добавлением его в группу 'sudo'.
    user:
      name: divitcfg
      password: $hashed_password
      shell: /bin/bash
      groups: sudo
      append: yes
    when: ansible_os_family == "Debian"

  - name: Добавить пользователя 'divitcfg' с добавлением его в группу 'wheel'.
    user:
      name: divitcfg
      password: $hashed_password
      shell: /bin/bash
      groups: wheel
      append: yes
    when: ansible_os_family == "RedHat"

#  - name: Создать 2048-битовый SSH ключ для lnxcfg в ~lnxcfg/.ssh/id_rsa
#    user:
#      name: lnxcfg
#      generate_ssh_key: yes
#      ssh_key_bits: 2048
#      ssh_key_file: .ssh/id_rsa

  - name: Установить authorized key из файла id_rsa.pub
    authorized_key:
      user: divitcfg
      state: present
      key: "{{ lookup('file', '/root/.ssh/id_rsa.pub') }}"
EOF

ansible-playbook -i inventory_add_user.txt -u $host_root_login -e ansible_sudo_pass=$host_root_password playbook_add_user.yml

rm -f inventory_add_user.txt playbook_add_user.yml
