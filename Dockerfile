FROM python:3.12-slim

ARG VERSION
ENV SETUPTOOLS_SCM_PRETEND_VERSION=$VERSION
RUN apt-get update \
     && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \
    gcc \
    libnetcdf-dev \
    && pip3 install --no-cache-dir --upgrade pip cython uv \
    && apt-get purge -y --auto-remove gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Create a new user
RUN adduser --quiet --disabled-password --shell /bin/sh \
--home /home/dockeruser --gecos "" --uid 1000 dockeruser

RUN mkdir -p /worker && chown dockeruser /worker

WORKDIR /worker

COPY --chown=dockeruser:dockeruser pyproject.toml README.md LICENSE ./
COPY --chown=dockeruser:dockeruser casper ./casper
COPY --chown=dockeruser:dockeruser uv.lock ./
COPY --chown=dockeruser:dockeruser docker-entrypoint.sh ./

USER dockeruser
RUN uv sync --extra harmony --frozen

RUN chmod +x ./docker-entrypoint.sh

# Run the service
ENTRYPOINT ["./docker-entrypoint.sh"]
