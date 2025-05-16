FROM jenkins/jenkins:lts-jdk17

USER root

# Instalar herramientas necesarias
RUN apt-get update && apt-get install -y \
    docker.io \
    git \
    python3 \
    python3-pip \
    python3-venv \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
