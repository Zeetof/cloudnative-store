# CloudNative Store - Product Service

This is the **Product Service** for the CloudNative Store DevOps project.

## Features
- Simple Flask API serving a list of products
- Dockerized service
- CI pipeline with GitHub Actions (build, test, push to DockerHub)

## Run locally
```bash
cd app/product-service
pip install -r requirements.txt
python app.py
```
Then open `http://127.0.0.1:5000/products`

## Run with Docker
```bash
docker build -t product-service .
docker run -p 5000:5000 product-service
```

## CI/CD
This repo includes a GitHub Actions workflow that:
- Runs tests
- Builds Docker image
- Pushes to DockerHub
