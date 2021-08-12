# Authenticated-TorSite

Developed and deployed a smart home webapp on Tor as an authenticated service hosted on a Raspberry Pi. The project involved piping connectivity data from locally connected ESP8266 devices (could be any IoT or smart device) to a webapp via a python program/script. The python program then uses flask to pipe that data to and render an HTML page (using Javascript) which further used JQuery and CSS to display connectivity, temprature and proxy time information in a visually appealing manner. The website is hosted using Nginx which has been configured to allow interoperability between the python program and the server using UWSGI. The Nginx server is then deployed as a TOR hidden service. To add a layer of security, public/private key pairs are generated for the authorized clients to only allow select indiviuals to access the Tor Site. 

This project was a proof of concept where TOR is used to enhance smart device security by shutting down WAN based vulnerabilities. Often time, when users connect to local smart devices over WAN, they expose sensitive information such as IP addresses and more. Onion routing allows same form of access but without exposing any sensitive information at all, and only allowing certain users access, even if multiple users know the onion url. 

A large amount of this project was configuration file writing, bash scripting and raspbian OS developing. 

--- Links & Development Questions ------

Q: Currently using cron and a bash script to update data (such as temprature and proxy time) on the server every 5 mins, are there better options? 

Links: 

Tor & Onion Routing: https://www.torproject.org/
UWSGI: https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
Nginx: https://www.nginx.com/
Flask: https://flask.palletsprojects.com/en/2.0.x/
