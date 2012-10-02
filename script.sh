#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/dev2.log
#NUM_WORKERS=3
NUM_WORKERS=4
# user/group to run as
USER=root
GROUP=root
cd /home/projects/dev2/love2travel
source ../bin/activate
exec /home/projects/dev2/bin/gunicorn_django -b 31.131.16.181:9090 -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE

