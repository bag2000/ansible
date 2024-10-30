#!/bin/sh

OK=e8bf71
RED=ff3300
UP="%{F#$OK}Mail(0)"
DOWN="%{F#$RED}Mail"

updates=$(cat ~/polybar-scripts/mail/mail_check.txt);

if [ "$updates" -gt 0 ]; then
    echo "$DOWN($updates)"
else
    echo "$UP"
fi