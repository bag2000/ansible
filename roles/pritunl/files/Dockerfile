FROM ubuntu:latest
RUN apt-get update && \
    apt-get upgrade -y && \
    echo deb http://repo.pritunl.com/stable/apt jammy main > /etc/apt/sources.list.d/pritunl.list && \
    apt-get install -y gnupg && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv 7568D9BB55FF9E5287D586017AE645C0CF8E292A && \
    apt-get install -y nano
RUN echo ***********************************
RUN apt-get update && apt-get -y install pritunl
COPY ./startbind.sh ./startbind.sh
ENTRYPOINT [ "./startbind.sh" ]
