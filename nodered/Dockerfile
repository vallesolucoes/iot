FROM nodered/node-red:latest

#COPY nodered/settings.js /node-red-data/settings.js
COPY settings.txt /node-red/texto.txt
#COPY settings,txt /mosquitto/config/settings.txt
# cd /var/lib/docker/volumes/iot3_node-red-data/_data

RUN npm install node-red-contrib-whatsapp-link

RUN apt-get clean && rm -rf /var/lib/apt/lists/*
