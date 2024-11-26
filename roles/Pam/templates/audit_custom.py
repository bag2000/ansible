from datetime import datetime
import subprocess
import logging
from logging.handlers import SysLogHandler

sysloghHandlr = SysLogHandler(address=("192.168.39.100", 514))

# Записываем в лог
def log_save(msg: str):
    with open('/var/log/audit_custom.log', 'a') as file:
        file.write(msg)

# Выполняем команду в linux
def run_cmd(cmd: str):
    ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = ps.communicate()
    stdout = stdout.decode("utf-8")
    stderr = stderr.decode("utf-8")
    out = {
        "stdout": stdout,
        "stderr": stderr
    }
    return out

# Получаем имена (list) всех интерфейсов
eth = run_cmd('ls /sys/class/net')
eth_list = eth['stdout'].strip().split()

# Получаем мак и ip каждого интерфейса
eth_full = ""
for eth in eth_list:
    if eth != "lo":
        eth_name = eth
        eth_mac = run_cmd(f"ip address show {eth}" + " | grep ether | awk '{print $2}'")['stdout'].strip()
        eth_ip = run_cmd(f"ip address show {eth}" + " | grep -w inet | awk '{print $2}'")['stdout'].strip()

        if eth_ip != '':
            eth_full += f"{eth_name} {eth_mac} {eth_ip}; "
        else:
            eth_full += f"{eth_name} {eth_mac}; "

#Проверяем, входит ли пользователь или выходит
pam_type = run_cmd("echo $PAM_TYPE")['stdout'].strip()

if pam_type == "open_session":
    session="loggin"
else:
    session="logout"

hostname = run_cmd('hostname')['stdout'].strip()
#user = run_cmd('whoami')['stdout'].strip()
date = datetime.today().strftime('%d.%m.%Y %H:%M:%S')
tty = run_cmd("echo $PAM_TTY")['stdout'].strip()
service = run_cmd("echo $PAM_SERVICE")['stdout'].strip()

if "tty" in tty:
    user = run_cmd('echo $USER')['stdout'].strip()
else:
    user = run_cmd('whoami')['stdout'].strip()

# Отправляем лог, если имя пользователя не gdm (login manager)
if user != "gdm":
    log = f'{date} {hostname} {user} {session} {tty} {service}; {eth_full}\n'
    #log_save(log)
    logger = logging.getLogger()
    logger.addHandler(sysloghHandlr)
    logger.setLevel(logging.INFO)
    logger.info(f" {log} ")