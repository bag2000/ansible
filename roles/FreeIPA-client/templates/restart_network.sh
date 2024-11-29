#!/bin/bash

/usr/bin/nmcli con down {{ conn }} && /usr/bin/nmcli con up {{ conn }}