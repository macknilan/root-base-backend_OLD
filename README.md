# Root-base-backend

:construction: Documentation in progress :construction:

API project that serves as the basis for user administration for different types of projects carried out with  
:link: :octocat: [cookiecutter-django](https://github.com/pydanny/cookiecutter-django)

The documentation :notebook: of the API is made with _Postman_ ![POSTMAN](https://github.com/postmanlabs/postman-docs/blob/develop/src/images/favicon.png "POSTMAN")

:link: [Rootbase-backend :notebook:](https://documenter.getpostman.com/view/8810189/TVCh1Tmu)

![https://github.com/pydanny/cookiecutter-django/](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg "Built with Cookiecutter Django")
![https://github.com/ambv/black](https://img.shields.io/badge/code%20style-black-000000.svg "Black code style")

| License | MIT |
| ------- | --- |

The objective of this project is to have an API with Django that initially serves for user administration (CRUD) and later the business logic is implemented, which requires user administration.

### :house: Cookiecutter Django Settings :link: [link](https://cookiecutter-django.readthedocs.io/en/latest/index.html)

```bash

```

### Commands for Docker :whale2: to work with :link: :octocat: [cookiecutter-django](https://github.com/pydanny/cookiecutter-django)

#### Basic Docker

```bash
$ docker images
$ docker container
$ docker volume
$ docker network
# PARA CADA UNO
ls
rm
prune
-a
-q
```

#### Docker images

Listar todos las imagenes

```bash
docker images -a
```

#### Docker containers

List all containers

```bash
$ docker container ls -a
```

Stop all containers

```bash
$ docker container stop $(docker container ls -aq)
```

Stop and delete all containers

```bash
$ docker container rm $(docker container ls -aq)
```

Delete all containers stoped, images and networks unused

```bash
$ docker system prune
```

Delete all volumes unused

```bash
$ docker system prune --volumes
```

#### Some commands of `docker-compose`

```bash
# COMPOSE_FILE
$ export COMPOSE_FILE=local.yml

$ docker-compose build
$ docker-compose up
$ docker-compose ps
$ docker-compose down
```

#### Docker-compose imagenes

```bash
# Para construir las imagenes
$ docker-compose -f local.yml build

# Para correr el stack
$ docker-compose -f local.yml up

# Para ver el estado de los procesos de Docker
$ docker-compose -f local.yml ps

# Para detener la ejecución
$ docker-compose -f local.yml down
```

#### Administration commands

La bandera `--rm` lo que hace es que crea un contenedor solo para el fin indicado y cuando acabe de ejecutarse el comando **mata el contenedor**

```bash
# Para correr comandos de Django usamos
docker-compose run --rm django COMMAND
#
# Por ejemplo para crear un super usuario
docker-compose run --rm django python manage.py createsuperuser
```

#### Make debugger

```bash
# 1 Para correr el stack de contenedores
# -f, --file FILE             Specify an alternate compose file
$ docker-compose -f local.yml up
```

```bash
# 2 Saber con que nombre esta el contenedor
# -f, --file FILE             Specify an alternate compose file
# ps List containers
$ docker-compose -f local.yml ps
```

```bash
# 3 MATAR EL DOCKER DJANGO
# -f, --force     Force the removal of a running container (uses SIGKILL)
# -l, --link      Remove the specified link
# -v, --volumes   Remove anonymous volumes associated with the container
$ docker rm -f <ID>
```

```bash
# 4 DESPUES DE SACAR/MATAR EL DOCKER DE django PARA LEVANTAR LO DE NUEVO ES
# run Run a one-off command
# rm Remove stopped containers
$ docker-compose -f local.yml run --rm --service-ports django
# Hacer migraciones
$ docker-compose -f local.yml run --rm django python manage.py makemigrations
# Migrar a la BD
$ docker-compose -f local.yml run --rm django python manage.py migrate
# EJEMPLO PARA CREAR SUPER-USUARIO
$ docker-compose -f local.yml run --rm django python manage.py createsuperuser
# Entrar al shell de django +
$ docker-compose run --rm django python manage.py shell_plus
# Cuando se presentan problemas con las migraciones y una opción es que se elimine el "volumen" de la BD donde se almacena la data tiene la terminación NOMBRE DEL PROYECTO_postgres_data
#Primero se tiene que detener la ejecucion de docker-compose
$ docker-compose -f local.yml down
# Mostrar los volunenes de docker
$ docker volume ls
# Eliminar el volimen NOMBRE DEL PROYECTO_postgres_data
$ docker volume rm NOMBRE DEL PROYECTO_postgres_data
```
