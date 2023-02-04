#!/bin/bash
while true
do
	echo -n "$(date) " >> openFiles.log
    bash -c "sysctl fs.file-nr" >> openFiles.log
    sleep 10
done