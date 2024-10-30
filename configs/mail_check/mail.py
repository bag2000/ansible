import imaplib
import time

boxes = ['INBOX', '1C', 'Carbonio', 'Doc1c', 'ITSM', 'No-reply', 'Synology', 'TechExpert', 'Veeam', 'Vzdump', 'Zabbix']
path = "/home/adm2/polybar-scripts/mail/mail_check.txt"

mail_pass = "password"
username = "mail@ya.ru"
imap_server = "imap.mail.ru"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, mail_pass)

while True:
    mail_count = 0
    for box in boxes:
        imap.select(f'{box}')

        unseen_mails = imap.search(None, "UNSEEN")
        mail_byte = str(unseen_mails[1])
        mail_byte = mail_byte.replace("b", "")
        mail_byte = mail_byte.replace("[", "")
        mail_byte = mail_byte.replace("]", "")
        mail_byte = mail_byte.replace("'", "")
        mail_list = mail_byte.split(" ")

        if mail_list[0] != "":
            mail_count += len(mail_list)

    with open(path, 'w') as file:
        file.write(str(mail_count))

    time.sleep(10)