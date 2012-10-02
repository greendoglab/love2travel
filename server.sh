#!/bin/bash

case "$1" in

 "start") 
 ./manage.py runfcgi method=prefork host=127.0.0.1 port=8011 pidfile=/tmp/wsgi.pid 

 ;;

 "stop") 

 kill -9 `cat /tmp/wsgi.pid` 

 ;;

 "restart")

 $0 stop

 sleep 1

 $0 start

 ;;

 *) echo "Usage: ./server.sh {start|stop|restart}";;

esac

