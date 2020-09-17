FROM quay.io/jupyteronopenshift/s2i-minimal-notebook-py36:2.5.1

USER root

COPY . /tmp/src

RUN rm -rf /tmp/src/.git* && \
    chown -R 1001 /tmp/src && \
    chgrp -R 0 /tmp/src && \
    chmod -R g+w /tmp/src && \
    rm -rf /tmp/scripts && \
    mv /tmp/src/.s2i/bin /tmp/scripts && \
    mkdir -p /usr/src/root && \
    chown -R 1001 /usr/src/root && \
    chown -R 1001 /usr/local/lib

ENV XDG_CACHE_HOME=/opt/app-root/src/.cache

RUN yum install -y epel-release \
 && yum install -y git cmake3 gcc-c++ gcc binutils \
  libX11-devel libXpm-devel libXft-devel libXext-devel openssl-devel \
  python36-devel \
 && localedef -i en_US -f UTF-8 en_US.UTF-8

USER 1001

#RUN pip install python-dev-tools

RUN cd /tmp \
 && git clone --depth 1 --branch v6-22-00-patches https://github.com/root-project/root /usr/src/root \
 && cmake3 /usr/src/root \
  -DPYTHON3=ON \
	-DPYTHON_EXECUTABLE=/opt/app-root/bin/python3 \
  -DPYTHON_INCLUDE_DIR=/opt/app-root/include/python3.6m \
  -DPYTHON_LIBRARY=/opt/app-root/lib/python3.6/site-packages \
 && cmake3 --build . -- -j$(nproc) \
 && cmake3 --build . --target install \
 && rm -rf /usr/src/root \
 && cd -

ENV PYTHONPATH /usr/local/lib

RUN /tmp/scripts/assemble

CMD [ "/opt/app-root/builder/run" ]
