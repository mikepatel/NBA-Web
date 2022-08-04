# NBA-Web
## Overview
A simple web app

## Dataset
* Dataset courtesy of [Justinas Cirtautas](https://www.kaggle.com/datasets/justinas/nba-players-data)

## Instructions
### MongoDB server (over Docker)
1. Start Docker Desktop
2. Build docker image (e.g. called `mongodb`)
```
docker build -t <image name> <path to Dockerfile>
```

2. Start MongoDB server
```
docker run --name <container name> -p <host port>:<container port> -v <host volume file path>:/data/db <image name>
```

3. Open MongoDB Compass
4. Connect to the running instance
5. Using MongoDB Compass, import the csv data located in `data`

### Web app
#### Virtual environment
1. Create a new virtual environment using pipenv (navigate to specific directory)
```
pipenv --python 3
```

2. Activate the new environment (used Windows)
```
pipenv shell
```

3. Install python packages into the environment
```
pipenv install -r .\requirements.txt
```

#### Start web app
1. Start the server (in debug mode)
```
uvicorn run:app --reload
```

### Test Endpoints
1. Used Postman to test endpoints
