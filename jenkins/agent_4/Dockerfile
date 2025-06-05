FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    docker.io \
    git \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    unzip \
    && python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install flake8 bandit locust \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PATH="/opt/venv/bin:$PATH"

RUN usermod -aG docker jenkins
USER jenkins
