Role Name
=========

Устанавливает pritun и mongodb. Логин / пароль - admin / admin.

Role Variables
--------------

upgrade - обновить все пакеты на сервере (true для обновления)

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: pritunl, upgrade: true }
