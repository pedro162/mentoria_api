FROM python:3.13-slim

ARG UID=1000
ARG GID=1000


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential libpq-dev --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Criar usuário com o mesmo UID e GID do host
RUN groupadd -g ${GID} appgroup && \
    useradd -m -u ${UID} -g ${GID} -s /bin/bash appuser

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar código com as permissões corretas
COPY --chown=appuser:appgroup . /app

# Trocar para o usuário normal
USER appuser

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]