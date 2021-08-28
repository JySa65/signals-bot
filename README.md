# Signals bot

## Signals bot using Binance API 
----
## Requeriments

- Git
- Docker
- Docker Compose
- Python 3

## Install

1. docker
2. docker-compose


## Create file .env and Edit

```sh
cp .env.example .env
```
```sh
nano .env
```

## Create docker image Project

- Create build by docker

```sh
./run build
```

## Development

### Migrations

```sh
./run migrate
```
### Create Superuser

```sh
./run command createsuperuser
```

### Start

```sh
./run up
```

### Stop

```sh
./run down
```
