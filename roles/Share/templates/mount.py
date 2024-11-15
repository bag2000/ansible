import subprocess
import time

while True:
    cmd_1 = 'df -h | grep -c /mnt/SharedDocs/{{ dst_share_name }}'
    ps_1 = subprocess.Popen(cmd_1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    stdout, stderr = ps_1.communicate()
    out = stdout.decode("utf-8").strip()

    if out == '0':
        cmd_2 = '/usr/bin/kinit -k -t /etc/krb5-2.keytab {{ kytab_user }}'
        cmd_3 = 'mount -t cifs -o sec=krb5,multiuser,file_mode=0600,dir_mode=0700 //{{ srv_name_lower }}{{ share_name_modded }} /mnt/SharedDocs/{{ dst_share_name }}'

        ps_2 = subprocess.Popen(cmd_2, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        ps_3 = subprocess.Popen(cmd_3, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    time.sleep(10)