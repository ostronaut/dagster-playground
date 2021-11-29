# dagster-playground
Dagster and dagit applications playground.

## Docker image set up
To run test application in your local docker, please first create corresponding image. To do that, jsut run: `docker build -t dagster-playground:latest .`. Right after, it's possbile to run docker container: `docker run --name dagster -p 3000:3000 -d dagster-playground:v1`.

__Note__: It is also possible to pull image from docker hub. To do that, run the following: `docker pull ostronaut/dagster-playground:latest`. And to run container: `docker run --name dagster -p 3000:3000 -d ostronaut/dagster-playground:latest`.

After container is running, you can access Dagit UI by this link: http://localhost:3000/

## Tests
To run tests, please execute the following: `poetry run pytest tests/`.
