FROM python:3.10 as builder

WORKDIR /app
COPY    ./requirements.txt   /app/requirements.txt
RUN    pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


FROM python:3.10-slim
ENV PYTHONUNBUFFERED 0
WORKDIR /app

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache-dir /wheels/*

COPY    ./api /app/api
COPY    ./start.sh  /app/start.sh
RUN    chmod +x /app/start.sh

# Get Arguments
ARG ENVIRONMENT
ARG COMMIT_REF

# Set Environment
ENV ENVIRONMENT=$ENVIRONMENT
ENV COMMIT_REF=$COMMIT_REF

CMD    ["sh", "start.sh"]