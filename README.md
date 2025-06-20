# FastAPI with Database Example Project

## Prerequisites
- uv
- docker

## Folder Structure
```plaintext
.
├── .dockerignore              # Files to exclude from Docker build context
├── .gitignore                 # Git ignored files and directories
├── .python-version            # Python version pinning (e.g., for pyenv/uv)
├── docker-compose.yml         # Docker Compose configuration file
├── Dockerfile                 # Dockerfile for building FastAPI app container
├── main.py                    # Entry point for the FastAPI application
├── pyproject.toml             # Project dependencies and configuration
├── README.md                  # Project documentation
├── uv.lock                    # Lockfile for Python dependencies (used by uv)
└── mysql_data/                # Persistent volume directory for MySQL data
```


## Setup Instructions

### Clone the repository
```bash
git clone https://github.com/poonnachit-devops/fastapi-with-database.git
cd fastapi-with-database
```
this will create a directory named `fastapi-with-database` and navigate into it.

### How to install package
``` bash
uv add <package_name>
```
for example:
```bash
uv add pandas
```

### Develop Environment Setup
```bash
docker compose -f ./docker-compose.dev.yml up --watch
```
this command will start the development environment with live reloading enabled.

### Production Environment Setup
1. copy docker-compose.prod.yml to server
2. change fastapi_app image to your image
3. then run
```bash
docker compose -f ./docker-compose.prod.yml up
```
after run you will have
- mysql database
- phpmyadmin
- your fastapi app

### Access the Application
- FastAPI Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
- PhpMyAdmin: [http://localhost:9090](http://localhost:9090)