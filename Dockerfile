from debian

run apt update
run apt install -y python3 python3-pip

copy requirements.txt /requirements.txt

run pip3 install -r /requirements.txt

copy Corrida_matinal.gpx /Corrida_matinal.gpx
copy prints.py /prints.py

cmd python3 /prints.py
