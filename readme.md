# Ahorcado - Backend

[![Build Status](https://travis-ci.com/brunocaracini/TP-Agiles-2020-Backend.svg?branch=master)](https://travis-ci.com/brunocaracini/TP-Agiles-2020-Backend)
[![codecov](https://codecov.io/gh/brunocaracini/TP-Agiles-2020-Backend/branch/master/graph/badge.svg?token=NV5JRFA9UU)](https://codecov.io/gh/brunocaracini/TP-Agiles-2020-Backend)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=brunocaracini_TP-Agiles-2020-Backend&metric=alert_status)](https://sonarcloud.io/dashboard?id=brunocaracini_TP-Agiles-2020-Backend)


Este Ahorcado fue realizado como trabajo práctico integrador de la asignatura Metologías Ágiles para el Desarrollo de Software, perteneciente al quinto año de la carrera Ingeniería en Sistemas de Información en la Universidad Tecnológica Nacional FRRo.

<h2> Descripción del Sistema </h2>

Ahorcado que permite jugar recreando las clásicas temrinales de juegos Arcade, permitiendo al usuario seleccionar una dificultad, un alias, y guardar el puntaje obtenido en la partida en caso de ganar.

<h2> Datos de Grupo de Trabajo </h2>

- Caracini,‌ ‌Bruno‌ ‌Tomás‌ ‌(43719)‌ ‌-‌ ‌‌bruno98980@gmail.com <br/>
- García,‌ ‌Santiago ‌(43685)‌ ‌-‌ ‌‌santiago.garcia181@gmail.com <br/>

<h2> Entorno de Desarrollo del Backend y Funcionamiento </h2>

El Backend de este Ahorcado fue desarrollado en Flask, que es un framework minimalista de Python que permite crear aplicaciones web rápidamente y con un mínimo número de líneas de código. Para comunicarse con el frontend, se crearon rutas (endpoints), los cuales responden ante un POST con un JSON que contiene la información requerida.
Para el almacenamiento de datos se utilizó MongoDB, con su correspondiente librería de Python, PyMongo. A su vez, se hosteó la BD en Atlas para poder acceder a ella de forma remota.

<h2> Unit Testing </h2>

Se utilizó la librería Pytest para llevar a cabo los Test Unitarios a lo largo del backend de la aplicación. Esta librería brinda además un porcentaje de código cubierto por estos tests (Code Coverage), en base al cual se integró la herramienta CodeCov que genera reportes visuales acerca el estado del Code Coverage en cada commit realizado en este repositorio.

<h2> Host, Puesta en Producción y CI Server</h2>

Se utilizó Heroku para hostear el backend de la aplicación y ponerla en producción, ya que además de ofrecer un servicio gratuito, tiene soporte para trabajar con Servidores de Integración Continua (CI Servers). En este sentido, se utilizó Travis como servidor CI para llevar a cabo las pruebas de Unit Testing, y para gestionar los deploys hacia Heroku en base al resultado obtenido en estos tests.
