# Project README

## Overview

This project is a FastAPI application integrated with a Retrieval-Augmented Generation (RAG) system. It processes PDF documents to store embeddings in a PostgreSQL database with the `pgvector` extension and allows querying through a RESTful API.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
- **PostgreSQL**: A relational database management system.
- **pgAdmin 4**: A web-based interface for managing PostgreSQL databases.
- **Docker**: To run the `pgvector` Docker container.

### Setup PostgreSQL with `pgvector`

1. **Install Docker**: If you don't have Docker installed.
2. **Pull the `pgvector` Docker image**:
    ```bash
    docker pull ankane/pgvector
    ```

3. **Run the Docker container**:
    ```bash
    docker run --name pgvector-demo -e POSTGRES_PASSWORD=test -p 5432:5432 -d ankane/pgvector
    ```

4. **Verify that the container is running**:
    ```bash
    docker ps
    ```

5. **Connect to the PostgreSQL database**:
    - Use `pgAdmin 4` or `psql` to connect.
    - Host: `localhost`
    - Port: `5432`
    - Username: `postgres`
    - Password: `test`

6. **Create the database and enable `pgvector` extension**:
    ```sql
    CREATE DATABASE vector_db;
    CREATE EXTENSION pgvector;
    ```

### Install Required Python Packages

Install the required Python packages using pip:

```bash
pip install langchain-community langchain-huggingface ollama pypdf2 psycopg2-binary langchain sentence-transformers fastapi pydantic requests uvicorn transformers
Download and Set Up Ollama:

    Download the following Ollama models: lama3, phi, smollm.
    The smollm model is used in this project because its size and RAM requirements are suitable for most laptops.for more info about it :https://ollama.com/library/smollm/blobs/6cafb858555d
      
### Installation
Docker Setup

    Pull the pgvector Docker Image:

    bash

docker pull ankane/pgvector

Run the Docker Container:

bash

docker run --name pgvector-demo -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d ankane/pgvector

Verify the Docker Container is Running:

bash

    docker ps

PostgreSQL and pgvector Setup

    Access PostgreSQL Using pgAdmin or psql:
        Connect to the database with host localhost and password mysecretpassword.

    Create a Database and Enable pgvector:

    sql

CREATE DATABASE vector_db;
\c vector_db;
CREATE EXTENSION pgvector;

    Note: If you are not using the Docker image provided, you will need to install the pgvector extension .
    Running the Application

    Start the Docker Container:

    bash

docker start pgvector-demo

Connect to the Database:

    Use pgAdmin4 or psql to connect to localhost:5432 with the database vector_db.

Run the FastAPI Application:

bash

uvicorn main:app --reload
    You can also test the endpoints using the Swagger UI at http://127.0.0.1:8000/docs..
    Project Structure

bash

.### Project Structure
├── api.py               # FastAPI application
├── pdf_processing.py     # PDF preprocessing functions
├── rag_agent.py      # Agent System
├── README.md             # Project documentation
└── ...

### Acknowledgements

    LangChain for providing the core libraries used in this project.
    Ollama for the language model API.
    pgvector for enabling vector similarity searches in PostgreSQL.