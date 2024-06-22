FROM ollama/ollama:latest

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends && \
    apt-get install -y python3 python3-pip

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY start.sh /tmp/start.sh

RUN chmod +x /tmp/start.sh

ENTRYPOINT ["/tmp/start.sh"]
