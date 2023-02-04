#!/bin/bash
while true
do
    du --max-depth=0 ./results/ >> hddMon.log
    sleep 120
done