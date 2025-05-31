FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    docker.io \
    git \
    python3 \
    python3-pip \
    python3-venv && \
    pip3 install --no-cache-dir flake8 bandit && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN usermod -aG docker jenkins

USER jenkins