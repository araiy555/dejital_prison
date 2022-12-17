FROM --platform=linux/x86_64 postgres:12

RUN \
    apt-get update && \
    apt-get -y install iproute2 net-tools \
    --no-install-recommends