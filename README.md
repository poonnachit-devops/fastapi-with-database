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

### Develop Environment Setup
```bash
docker compose up --watch
```
this command will start the development environment with live reloading enabled.

### Production Environment Setup
```bash
docker compose up
```

### Access the Application
- FastAPI Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
- PhpMyAdmin: [http://localhost:9090](http://localhost:9090)