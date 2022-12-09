FROM nodered/node-red:latest

#COPY nodered/settings.js /node-red-data/settings.js

#RUN docker volume create nodered
#RUN cp /iot/nodered/settings.txt /var/lib/docker/volumes/iot_nodered/_data/settings.txt
#RUN cp ./config/a.txt /a.txt

COPY ./settings.txt /var/lib/docker/volumes/iot_nodered/_data/settings.txt
# cd /var/lib/docker/volumes/iot3_node-red-data/_data

#RUN npm install node-red-contrib-whatsapp-link
#RUN npm install node-red-contrib-telegrambot
#RUN npm install node-red-node-mysql
