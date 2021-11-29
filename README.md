# dagster-playground
Dagster and dagit applications playground.

## Docker image set up
To run test application in your local docker, please first create corresponding image. To do that, jsut run: `docker build -t dagster-playground:latest .`. Right after, it's possbile to run docker container.

## Tests
To run tests, please execute the following: `poetry run pytest tests/`.
