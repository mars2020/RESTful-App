FROM python:3-onbuild
RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y redis-tools
# Do we need to do pip install -r requirements here or in main.py?
EXPOSE 5000
CMD ["python", "./main.py"]

