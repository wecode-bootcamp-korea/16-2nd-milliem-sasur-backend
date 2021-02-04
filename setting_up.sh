#!/bin/sh

#make virtual_envorionment
echo y | conda create -n milliem python=3.9 && conda activate milliem

#install dependncy_packages
pip install -r requirements.txt

#make_database  models.py 파일이 사전에 --rds의 db와 동기화 되어있어야함.
python manage.py migrate

echo "your_server_IP_address"
echo | curl ifconfig.me 

#runserver_finally
python manage.py runserver 0:8000
