FROM centos:latest

LABEL version="2.0" maintainer="mccbryan.ops@gmail.com"

RUN  ["mkdir", "/twr_je_hvst/logs", "-p"]
COPY twr_je_hvst_li_v2.py /twr_je_hvst/
COPY get-pip.py /twr_je_hvst/

RUN ["yum", "install", "epel-release", "-y"] 
RUN ["yum", "install", "python36", "-y"] 
RUN ["python3", "/twr_je_hvst/get-pip.py"] 
RUN ["pip3", "install", "requests"]

ENTRYPOINT ["python3", "/twr_je_hvst/twr_je_hvst_li_v2.py"]
