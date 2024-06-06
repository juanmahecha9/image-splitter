# Como hacer un deploy de aplicaciones python en heroku

Para hacer el deploy se requeire seguir los siguientes pasos:

1. Crear una carpeta que contendra el proyecto `mkdir folder_name && cd folder_name`
2. Crear el entorno de desarrollo `pip install virtualenv` y seguido iniciar el ambiente con `virtualenv env_name`
3. ejecutar el entorno `. env_name/bin/actiavte`
4. Instalar las dependencias que se requieran
5. Instalar GUINICORN (permite las conexiones con heroku) `pip install gunicorn`
6. Crear folder del proyecto `mkdir project` en el se crea el proyecto, para el despliegue es necesario que el puerto este ejecutandoce en el puerto 5000 y los debug en false
7. Dirigirce al folder del projecto `cd project` y crear un archivo de ejecucion de que paquetes son requeridos en el proyecto, este archivo se crea con el comando `pip freeze > requirements.txt`
8. Crear el archivo prockfile, este archivo no tendra ninguna extencion y dentro de el se coloca la siguiente informaciòn, donde se estable que archivo se va a ejecutar como servidor esta informacion es: `web: gunicorn (main_file_name):app``
9. Para realizar el deploy, se requiere tener una cuenta en heroku, y descargar el toolbars en la maquina, al tener esto listo, se ejecuta el siguiente comando `heroku create` comando que ejecuta una nueva aplicacion
10. Seguir los pasos que heroku da para el deploy los cuales son: `git init`, `heroku git:remote -a (application_name)`, `git add .`, `git commit -am "message"`, git push heroku master``

Al finalizar esos pasos ya tendremos la aplicacion expuesta a internet para poder consumirla.