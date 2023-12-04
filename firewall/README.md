Role Name
=========

Настраивает фаервол, таблицу INPUT для всех и/или одного определенного ip
Открывает все pritunl порты, если есть
Открывает ssh (включая не стандартный, если изменен)

Requirements
------------

Необходим пакет net-tools

Role Variables
--------------

packages - список пакетов, которые будут установлены на все версии Linux (по умолчанию ['net-tools'])
ports_tcp_for_all - список tcp портов для всех (по умолчанию ['10050','10051','55413','55415'])
ports_udp_for_all - список udp портов для всех (по умолчанию ['35623'])
ports_tcp_for_one - список tcp портов для определенного ip (по умолчанию ['22','80','443','3389','8006','55414'])
ports_udp_for_one - список udp портов для определенного ip (по умолчанию [])
ip: (по умолчанию '95.165.43.186')

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: firewall, ip: '192.168.12.17', packages: ['net-tools','nano'] }

Example Exec
----------------

ansible-playbook playbook1.yml -u adm2 [ --ask-pass -K ]
