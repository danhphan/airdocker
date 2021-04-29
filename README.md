### Requirement:
`docker`
`docker-compose`

### Set up env variable into .env
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

### Build docker images
docker-compose up airflow-init

### Run docker instance
docker-compose up

After that, open webrowser at http://0.0.0.0:8080/ to access airflow