#!/bin/bash
timestamp=$(date +"%d-%m-%Y %H:%M:%S")
pid=$(lsof -i :7889 | awk 'NR==2 {print $2}')
kill $pid
echo "Proceso eliminado: $pid @ $timestamp"

sleep 5

cd
cd code/ocean-super/
source venv/bin/activate
python app.py &
PID=$(pgrep -f "python app.py")
timestamp2=$(date +"%d-%m-%Y %H:%M:%S")
echo "Proceso reiniciado: $PID @ $timestamp2"
