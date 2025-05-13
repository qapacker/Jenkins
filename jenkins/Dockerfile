FROM jenkins/jenkins:lts-jdk17

USER root

# Instalar herramientas
RUN apt-get update && apt-get install -y \
    docker.io \
    git \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean

# Crear grupo docker si no existe (por si acaso)
RUN groupadd -f docker && usermod -aG docker jenkins

USER jenkins