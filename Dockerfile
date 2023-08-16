FROM python:3.10

LABEL name="MyTrader"
LABEL version="0.1.0"
LABEL description="My Trader Project!"

WORKDIR /app

ADD . ./

# CMD ["python"]