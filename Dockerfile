FROM python:3.5-onbuild

RUN apt-get clean && apt-get update 
RUN apt-get install -y  --fix-missing --no-install-recommends \
    sudo iceweasel xvfb
RUN rm -rf /var/lib/apt/lists/*

ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

RUN groupadd -g ${gid} ${group} \
            && useradd -d /home/jenkins -u ${uid} -g ${gid} -m -s /bin/bash ${user}

RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
