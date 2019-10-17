FROM ubuntu
USER root
RUN git clone https://github.com/JesterOrNot/pymath.git
RUN apt-get update && apt-get install python3-pip --yes
RUN pip3 install ipython3
RUN python3 setup.py install
SHELL [ "ipython3" ]
