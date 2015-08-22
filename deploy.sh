#!/bin/bash

nohup python app.py > log/ems.log &
sleep 1
echo server start, see log file in log/ems.log
