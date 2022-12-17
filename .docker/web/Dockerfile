FROM --platform=linux/x86_64 almalinux:8.6

RUN dnf -y update && \
    dnf -y install epel-release && \
    dnf -y groupinstall "Development Tools" && \
    dnf -y install wget git vim zsh curl && \
    rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-8.rpm && \
    dnf -y install openssl httpd httpd-devel mod_ssl && \
    dnf -y update && \
    dnf -y module reset php && \
    dnf -y module enable php:remi-8.1 && \
    dnf -y install php php-cli php-common php-fpm php-gd php-mysqlnd php-pdo php-pear php-pecl-imagick php-pecl-zip php-pgsql php-process php-soap php-xml && \
    dnf -y install ImageMagick-devel iproute && \
    dnf -y install postgresql
