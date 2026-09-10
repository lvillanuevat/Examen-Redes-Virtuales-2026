# Examen Redes Virtuales 2026

Repositorio privado de evidencias y scripts del examen de Redes Virtuales.

## Entorno

- Modalidad: grupal
- DEVASC: `192.168.43.23`
- CSR1000v: `192.168.43.200`
- Hostname CSR1000v: `VILLANUEVA-MEYER`
- Usuario CSR1000v: `admin`
- Flask local: `http://127.0.0.1:8000`
- Flask en Docker: `http://127.0.0.1:8888`

## Actividades realizadas

- Configuracion de Git y rama `desarrollo`.
- Script Python basico con variables del grupo.
- Aplicacion Flask con HTML/CSS.
- Contenedor Docker publicado en puerto `8888`.
- Validacion de conectividad entre DEVASC y CSR1000v.
- Activacion y prueba de SSH/RESTCONF.
- Creacion manual de `Loopback11` con `11.11.11.11/32`.
- Creacion RESTCONF de `Loopback44` con `44.44.44.44/24`.
- Creacion RESTCONF por Python de `Loopback55` con `172.16.55.1/24`.
- Eliminacion RESTCONF de `Loopback44`.
- Validacion por Netmiko con `show ip interface brief`, `show running-config` y `show version`.
- Evidencias visuales en `prints_examen_rv/`.

## Archivos principales

- `datos_grupo.py`: actividad Python de variables y mensaje.
- `app.py`: aplicacion Flask.
- `Dockerfile`: imagen Docker para Flask.
- `crear_loopback55.py`: creacion de Loopback55 por RESTCONF.
- `validar_router_netmiko.py`: validacion del router por SSH/Netmiko.
- `loopback44.json`: payload RESTCONF usado para Loopback44.
- `salida_netmiko.txt`: evidencia textual de comandos Netmiko.
- `prints_examen_rv/`: capturas del laboratorio.
