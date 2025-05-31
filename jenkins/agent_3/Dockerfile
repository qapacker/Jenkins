FROM jenkins/inbound-agent:latest

USER root

# Instala dependencias del sistema y crea un entorno virtual
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    docker.io \
    git \
    python3 \
    python3-pip \
    python3-venv && \
    python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir flake8 bandit && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Añade el entorno virtual al PATH
ENV PATH="/opt/venv/bin:$PATH"

# Añade al usuario jenkins al grupo docker
RUN usermod -aG docker jenkins

USER jenkins