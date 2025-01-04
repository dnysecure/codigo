#clic der on conexion - Open in integrate terminal
#install pip install mysql-connector-python

import mysql.connector

conexion = mysql.connector.connect(user='root', password='Prueba.123',
                                    host='172.17.1.131',
                                    database='prueba',
                                    port='3306')
print(conexion)

"""
#Instalando docker en wsl 2 Ubuntu
sudo apt install -y curl
curl -s https://raw.githubusercontent.com/karaage0703/ubuntu-setup/master/install-docker.sh | /bin/bash
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get -y install docker-ce docker-ce-cli containerd.io
sudo apt-get -y install docker-compose-plugin
sudo gpasswd -a $USER docker

# iniciando docker

sudo service docker start

# instalar la imagen mysql en el docker 
docker pull mysql
docker run --name mysql-prueba -e MYSQL_ROOT_PASSWORD=password -d mysql:latest
#entrar desde consola a mysql
docker exec -it mysql-prueba bash 
mysql -u root -ppassword

# abrir puertos para ingreso desde afuera

docker run --name mysql-prueba -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -d mysql:latest
# permitir acceso remoto
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';


#comandos mysql

Crear una base de datos: create database [databasename];
Listar todas las base de datos en el servidor: show databases;
Cambiar a una base de datos: use [db name];
Ver todas las tablas de una base de datos: show tables;
Ver los formatos de campo de la base de datos: describe [table name];
Eliminar una base de datos: drop database [database name];
Eliminar una tabla de la base de datos: drop table [table name];
Devolver todos los registros de una tabla: SELECT * FROM [table name];
Devolver las columnas y la información de la columna correspondiente a la tabla designada:
show columns from [table name];
Mostrar ciertas filas seleccionadas con el valor «lo que sea»:SELECT * FROM [table name] WHERE [field name] = «whatever»;

"""