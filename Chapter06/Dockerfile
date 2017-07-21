FROM python:3.6

RUN pip install circus chaussette

RUN apt-get -y update && \
    apt-get -y install libreadline-dev libncurses5-dev && \
    apt-get -y install libpcre3-dev libssl-dev perl make

RUN curl -sSL https://openresty.org/download/openresty-1.11.2.3.tar.gz \
    | tar -xz && \
    cd openresty-1.11.2.3 && \
    ./configure -j2 && \
    make -j2 && \
    make install

ENV PATH "/usr/local/openresty/bin:/usr/local/openresty/nginx/sbin:$PATH"

COPY docker/circus.ini /app/circus.ini
COPY docker/nginx.conf /app/nginx.conf
COPY docker/settings.ini /app/settings.ini
COPY docker/pubkey.pem /app/pubkey.pem
COPY docker/privkey.pem /app/privkey.pem

COPY . /app

RUN pip install -r /app/requirements.txt
RUN pip install /app/

RUN mkdir /logs
VOLUME /logs

EXPOSE 8080
CMD circusd /app/circus.ini
