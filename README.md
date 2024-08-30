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

    Download the following Ollama models: I used  lama3, phi, smollm. 
    
###Run the FastAPI Application:

bash

uvicorn main:app --reload
### test the endpoints

    You can also test the endpoints using the Swagger UI at http://127.0.0.1:8000/docs..
### Project Structure

bash


├── api.py               # FastAPI application
├── pdf_processing.py     # PDF preprocessing functions
├── rag_agent.py      # Agent System
├── README.md             # Project documentation
└── ...


**Acknowledgements**:

    LangChain for providing the core libraries used in this project.
    Ollama for the language model API.
    pgvector for enabling vector similarity searches in PostgreSQL.


**Examples of Queries and Response of model** 
Query: What are the responsibilities of the best candidate?

Response: The ideal candidate will have a strong background in natural language processing (NLP) and experience working with large language models (LLMs), LangChain, and vector databases. They will be responsible for developing, integrating, and deploying cutting-edge NLP solutions that leverage advanced AI technologies to enhance our products and services.


**COmment on Result**:
Among the available models, Llama3 delivers the best performance, followed by Phi, with Smollm being the least performant. However, I opted for Smollm due to its smaller size and faster execution, which allows it to run all components of the project concurrently. Llama3 requires more system memory (5.9 GiB) than is available on my system (3.7 GiB). Depending on your machine’s capabilities, you can choose any of the three models after downloading them. Simply specify the model name and run it, ensuring that you have first downloaded Ollama.
