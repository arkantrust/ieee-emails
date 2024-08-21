# Enviar emails a nuevos miembros del IEEE

Este repo contiene un programa en [python](https://python.org/) que usa el [SMTP de Gmail](https://support.google.com/a/answer/176600?hl=en) para enviar correos de bienvenida a los nuevos miembros de la rama estudiantil [IEEE](https://ieee.org) de la universidad [ICESI](https://www.icesi.edu.co/es/)  y optimizar el tiempo de los miembros del comité de recursos humanos y relaciones externas.

## Prerequisitos

### Google App Password

Es necesario obtener un token que le permita a Google autenticar el uso del SMTP server, para esto se debe:

- [Activar 2FA en la cuenta de Google](https://myaccount.google.com/u/0/signinoptions/twosv) desde donde se enviarán los correos
- Crear un Google App Password [aquí](https://myaccount.google.com/u/0/apppasswords).

### Archivo con información de miembros

De momento, los aspirantes se inscriben al IEEE mediante Google Forms, por lo que solo se debe descargar el archivo con las respuestas como un `.csv` desde Google Sheets y guardarlo en el mismo directorio de este repositorio como `new_members.csv`.

### Variables de entorno

Crear un archivo `.env` siguiende el [ejemplo](./.env.example).

## Running

Para correr la aplicación se puede crear un [python venv](https://docs.python.org/3/library/venv.html):

``` bash
$ python3 -m venv .venv # crea un venv en el directorio .venv

$ source ./.venv/bin/activate # inicia el venv

$ pip install -r requirements.txt # instala las dependencias

$ python3 main.py
```

> Estos comandos son específicos para Ubuntu, pero s similar para cualquier otro OS.
