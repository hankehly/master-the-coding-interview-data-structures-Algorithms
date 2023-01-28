# syntax=docker/dockerfile:1
FROM python:3.11
RUN <<EOT
  pip install -U pip
  pip install black isort
EOT
