#!/bin/sh

if [ -n "$TIMEZONE" ]; then
	echo $TIMEZONE > /etc/timezone
	dpkg-reconfigure --frontend noninteractive tzdata
fi

python /run.py
