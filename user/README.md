Role Name
=========

Создает NOPASSWD судо пользователя

Role Variables
--------------

ssh_key_path - путь к открытому ключу (по умолчанию: '/home/adm2/.ssh/id_rsa.pub')
user_name - имя учетной записи (по умолчанию: divitcfg)

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: user, ssh_key_path: '/home/adm2/.ssh/id_rsa.pub',  user_name: divitcfg }

Example Exec
----------------

ansible-playbook playbook1.yml -u adm2 --ask-pass -K