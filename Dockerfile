FROM ubuntu
USER root
RUN apt-get update && \
     apt-get install git \
        python3-pip --yes
RUN mkdir /app
WORKDIR /app
RUN git clone https://github.com/JesterOrNot/pymath.git
RUN pip3 install ipython3
RUN python3 setup.py install
CMD [ "ipython3" ]
