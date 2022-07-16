# Dockerfile

FROM python:3.8-buster

ENV DEBUG="False"

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY docker/nginx/nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/project_draw
RUN mkdir -p /opt/app/project_draw/static
COPY requirements.txt docker/server/start.sh docker/server/healthcheck.py /opt/app/

WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY src /opt/app/project_draw
RUN python /opt/app/project_draw/manage.py collectstatic
RUN chown -R www-data:www-data /opt/app

HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=3 \
    CMD [ "python", "/opt/app/healthcheck.py", "--port", "80" ]

# start server
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["/opt/app/start.sh"]
