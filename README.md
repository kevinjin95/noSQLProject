 
# noSQLProject

##  NoSQL project in Python, comparing 2 NoSQL batabase, 

## Download ressources

[here](https://unehistoireduconflitpolitique.fr/telecharger.html), then download the files of diploma to run politique.py

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies


##### Get your Redis's container and run it
```zsh
docker pull redis/redis-stack-server
docker run --rm redis/redis-stack-server:latest
```

##### Stop your Redis's container
```zsh
if you hadn't '-d', press ctrl+c to stop your container
```
```zsh
if you had '-d':
docker ps -a (to get the name of your container)
docker stop <container's name>
```
##### About Mongo 

You have to create an account on MongoDB's [website](https://www.mongodb.com)
then, create a database, get your token from MongoDB and paste it to a '.env' file

##### Activate your virtual environment:
```zsh
python3 -m venv env
source env/bin/activate
```

##### Windows:
```zsh
pip install -r requirements.txt
```

##### macOS/Linux:
```zsh
pip3 install -r requirements.txt
```

## Usage
#####

Before running your code, modify the path where you are gonna store the csv and json files

##### Windows:
```zsh
python main.py
```
##### macOS/Linux:
```zsh
python3 main.py
```
