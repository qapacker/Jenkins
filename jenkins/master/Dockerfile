FROM jenkins/jenkins:lts-jdk17

USER root

# Instalar herramientas necesarias en una sola capa y limpiar cache para reducir tamaño
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    docker.io \
    git \
    python3 \
    python3-pip \
    python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Añadir usuario jenkins al grupo docker para poder usar docker sin sudo
RUN usermod -aG docker jenkins

USER jenkins