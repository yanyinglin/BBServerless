FROM --platform=${TARGETPLATFORM:-linux/arm64} ghcr.io/openfaas/classic-watchdog:0.2.0 as watchdog
FROM --platform=${TARGETPLATFORM:-linux/arm64} python:3

ARG TARGETPLATFORM
ARG BUILDPLATFORM


RUN apt-get update \
    && apt-get install -y ca-certificates ${ADDITIONAL_PACKAGE} \
    && rm -rf /var/lib/apt/lists/

RUN pip install torch==1.12.0 torchvision==0.11.3 numpy  --target=/home/app/python

# Add non root user
RUN groupadd app && useradd -r -g app app

RUN chown -R app:app /home/app/
RUN chmod -R 777 /home/app/python