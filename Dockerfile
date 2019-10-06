FROM ubuntu
RUN pip3 install ipython3
RUN python3 setup.py install
SHELL [ "ipython3" ]