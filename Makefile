DOCKER_COMPOSE := $(shell which docker-compose)
DOCKER := $(shell which docker)

# Start development
up:
	$(DOCKER_COMPOSE) up

# Start development (detached mode)
upd:
	$(DOCKER_COMPOSE) up -d

# Down containers
down:
	$(DOCKER_COMPOSE) down

# Stop containers
stop:
	$(DOCKER_COMPOSE) stop

# Force build of docker
build:
	$(DOCKER_COMPOSE) build

# Delete containers
rm:
	$(DOCKER_COMPOSE) rm

# Pull docker images
pull:
	$(DOCKER_COMPOSE) pull

# Run unit tests locally (A .env file should be created in app folder with env vars needed)
test:
	$(DOCKER_COMPOSE) exec app bash -c "python -m pytest"

# Run code linter
lint:
	$(DOCKER_COMPOSE) run --rm app flake8

# Access to container bash
bash:
	$(DOCKER) exec -it app bash

# Generate migration file
migrate:
	$(DOCKER_COMPOSE) run --rm app alembic revision --autogenerate -m "$(msg)"

# Execute last migration file
exec-migration:
	$(DOCKER_COMPOSE) run --rm app alembic upgrade head"