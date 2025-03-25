FastAPI Template Starter
====================================

* A FastAPI template starter with folder structure to big projects
* SQLite database (local file) with alembic to manage migrations
* Black package was used as a code linter
* Docker is needed to run the app (please use Docker Desktop or Rancher Desktop)
* Logger is included
* Local file database is set in test folder

## Run local environment

To run the container please execute the following command:

    make up

Once the command is executed go to the following link http://localhost:8000, you are going to be redirected to API docs


## Other useful commands

Build docker image

    make build

Stop containers

    make stop

Stop containers

    make stop

Delete containers

    make rm

Run unit tests

    make test

Run black linter:

    make lint