# Variables
DOCKER_COMPOSE = docker-compose
DOCKER_COMPOSE_FILE = docker-compose.yml

# Default target
all: build run

# Build the Docker image
build:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) build

# Run the Docker containers
run:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up

# Stop and remove the Docker containers
stop:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down

# Clean up Docker resources (images, containers, volumes)
clean:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down --rmi all -v

# Execute the Python script inside the container
execute:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) run get_status

# Other targets can be added here for specific actions

.PHONY: build run stop clean execute py_run
