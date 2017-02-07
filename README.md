> (Besides of requirements.txt, list of packages to install via apt-get instead of pip and so)
> This **is not** the main README for the project. Just a guide for myself.

# [cloudmarket.es](https://cloudmarket.es/)

Paquetes a instalar en Debian/Ubuntu:
-------------------------------------
* python3-django
* python3-cookiecutter
* cookiecutter


Documentación:
--------------
* Repositorio en github: [cloudmarket.es](https://github.com/pacoqueen/cloudmarket.es)
* Submódulo proyecto Django 1.10: [cloudmarket](https://github.com/pacoqueen/cloudmarket)
* Plantilla proyecto: [Cookiecutter](https://github.com/pydanny/cookiecutter-django)
* Dominio: [Hostinet](https://www.hostinet.com/central/producto/103672/)
* Redirección DNS: [PointDNS](https://app.pointhq.com/zones/181000/records)
* Servidor de correo: [Mailgun](https://mailgun.com/app/domains/mg.cloudmarket.es)
* Alojamiento y cloud computing: [Heroku](https://dashboard.heroku.com/apps/qcloudmarket)
* Logs: [Sentry](https://sentry.io/app35222207herokucom/)
* Variables de entorno a establecer en heroku: [Cookiecutter deployment on Heroku](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html)
* Almacenamiento ficheros estáticos (se puede activar durante la creación del proyecto con Cookiecutter): [WhiteNoise](http://whitenoise.evans.io/en/stable/django.html)


Step by step (ooo, baby)
------------------------
1. Crear el proyecto cloudmarket.es en Github.
2. git clone
3. pyvenv cloudmarket.es
4. cookiecutter para crear el proyecto cloudmarket
5. pip install -r cloudmarket/requeriments.txt
6. pip install -r cloudmarket/requirements/local.txt
7. Crear el proyecto cloudmarket en Github.
8. Agregar cloudmarket como submódulo de cloudmarket.es
9. Crear el .env local en cloudmarket/config/settings/ basado en cloudmarket/env.example
10. Crear la *app* qcloudmarket en Heroku con el *buildpack* Python.
11. Activar en Heroku el despliegue automático basado en el repositorio de cloudmarket de Github.
12. Agregar el repositorio `git remote` de la *app* en Heroku a cloudmarket.
13. Establecer las variables de entorno con la CLI de heroku.
14. Commit de cloudmarket y cloudmarket.es
15. Si no se han creado con el despliegue, agregar los *addons* de PostgreSQL, Redis, Mailgun, PointDNS y Sentry y volver a establecer las variables de entorno si es necesario. Se puede hacer desde el terminal con, por ejemplo, `heroku addons:add sentry --app qcloudmarket`.
16. Cambiar las DNS del dominio para que apunten a PointDNS.
17. Crear los registros DNS de Mailgun en PointDNS.
18. Crear la base de datos local con `./manage.py migrate` y el superusuario con `./manage.py createsuperuser`.
19. Hacer lo mismo en Heroku:
```
heroku run python manage.py migrate
heroku run python manage.py check --deploy
heroku run python manage.py createsuperuser
```
Los errores de despliegue o ejecución se pueden ver en Sentry y con `heroku logs`.
