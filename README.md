![Header](assets/img/ryder_isologotipos.png)

# PIS - Aplicaciones Dash

Aplicaciones realizadas en python dash para proyecto PIS de Democracia en Red

- Módulo de Mapa de Zonificación Normativa 
- Módulo de Ranking Ambiental
- Módulo de Análisis estadístico de los censos

## Setup

Hay 2 maneras de preparar el entorno para desarrollo. A través de un entorno virtual de python, o a través de Docker

### 1 - Entorno virtual de python (virtualenv)

> #### ⚠️ Prerequisitos
> 
> Este entorno virtual requiere de:
> - [Python 3](https://www.python.org/)
> - [pip](https://www.pypi.org/)
> - [virtualenv](https://pypi.org/project/virtualenv/)

#### Instalación

Abrí una terminal del sistema en el directorio raiz del proyecto, creá el entorno virtual, activalo, instalá las dependencias del proyecto y ejecutá la plataforma

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

#### Ejecución

Abrí una terminal del sistema en el directorio raiz del proyecto, activá el entorno virtual y ejecutá la plataforma


```bash
$ source env/bin/activate
$ python main.py <tool>
```

tool puede ser alguna de las siguientes opciones:
- zonificacion
- censos
- ranking


### 2 - Docker

> #### ⚠️ Prerequisitos
> 
> Este entorno virtual requiere de:
> - [Docker](https://docs.docker.com/engine/install/_) y (docker) compose (que en las nuevas versiones ya viene en la instalación de docker)

#### Instalación

Abrí una terminal del sistema en el directorio raiz del proyecto y construí la imagen de docker

```bash
$ docker compose build
```

#### Ejecución

Abrí una terminal del sistema en el directorio raiz del proyecto y ejecutá la imagen en un contenedor

```bash
$ docker compose up
```

Para cambiar la herramienta que querés visualizar tenes que cambiar el command en docker-compose.yml

```yml
    command: python main.py <tool>
```

## Licencia

El siguiente repositorio es un desarrollo de codigo abierto bajo la licencia GNU General Public License v3.0. Pueden acceder a la haciendo [click aqui](./LICENSE).

