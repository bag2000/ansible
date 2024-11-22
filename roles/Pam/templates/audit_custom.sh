#!/bin/bash

#Получаем имена всех интерфейсов
eths=$(ls /sys/class/net)

# Получаем мак и ip каждого интерфейса
ETH_ALL=""
for eth in ${eths}; do
  if [ $eth != "lo" ]; then
    ETH_NAME="$eth"
    ETH_MAC="$(ip address show $eth | grep ether | awk '{print $2}')"
    ETH_IP="$(ip address show $eth | grep -w inet | awk '{print $2}')"
    ETH_ALL+="$ETH_NAME $ETH_MAC $ETH_IP; "
  fi
done

#Проверяем, входит ли пользователь или выходит
if [ "$PAM_TYPE" == "open_session" ]; then
  SESSION="loggin"
else
  SESSION="logout"
fi

#Если пользователь не gdm (логин мененджер), тогда отправляем лог
if [ $USER != "gdm" ]
then
  echo "$(date '+%d.%m.%Y %H:%M:%S') $(hostname) $IP $USER $SESSION; $ETH_ALL" >> /var/log/audit_custom.log
fi