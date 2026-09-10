# Indice de prints - Examen Redes Virtuales

Carpeta de trabajo en DEVASC: `~/examen_redes_virtuales`

Datos principales:
- DEVASC: `192.168.43.23`
- CSR1000v: `192.168.43.200`
- Usuario CSR: `admin`
- Router: `VILLANUEVA-MEYER`
- Flask local: `http://127.0.0.1:8000`
- Flask Docker: `http://127.0.0.1:8888`

Prints guardados:

1. `01_devasc_git_docker_8889.png`: estado inicial de DEVASC con trabajo Docker previo.
2. `02_csr_pantalla_negra_antes_reinicio.png`: CSR antes del reinicio, pantalla sin consola visible.
3. `03_devasc_docker_8888_ok.png`: Docker funcionando en puerto 8888 con respuesta HTTP 200.
4. `04_csr_arranque_tras_reinicio.png`: CSR iniciando despues del reinicio.
5. `05_csr_reinicio_post_boot_order.png`: evidencia adicional del arranque del CSR.
6. `06_csr_login_admin_check.png`: CSR disponible y solicitando acceso.
7. `07_csr_prompt_tras_enter.png`: pantalla de login del CSR.
8. `08_csr_show_ip_interface_brief.png`: CSR con IP `192.168.43.200` y loopbacks existentes.
9. `09_csr_enable_prompt.png`: acceso privilegiado al CSR.
10. `10_csr_restconf_loopback11_show.png`: SSH/RESTCONF y Loopback11 `11.11.11.11`.
11. `11_devasc_ping_restconf_get_loopback11.png`: DEVASC valida conectividad y GET RESTCONF.
12. `12_devasc_restconf_put_loopback44_201.png`: PUT RESTCONF crea Loopback44, HTTP 201.
13. `13_devasc_python_loopback55_201.png`: script Python crea Loopback55, HTTP 201.
14. `14_devasc_restconf_get_loopbacks_44_55.png`: GET RESTCONF valida Loopback44 y Loopback55.
15. `15_devasc_restconf_delete_loopback44_204.png`: DELETE RESTCONF elimina Loopback44, HTTP 204.
16. `16_devasc_netmiko_running_config.png`: Netmiko ejecuta comandos y muestra running-config.
17. `17_devasc_netmiko_resumen_version.png`: resumen Netmiko con interfaces y version IOS XE.
18. `18_devasc_postman_abriendo.png`: Postman abierto en DEVASC.
19. `19_postman_get_restconf_200_ok.png`: Postman ejecuta GET RESTCONF con Status 200 OK.

Pendiente para el informe:
- Confirmar nombres definitivos de integrantes para portada.
- Si el docente exige captura de PUT/DELETE dentro de Postman especificamente, repetir esas dos operaciones desde la interfaz de Postman; la ejecucion tecnica ya quedo validada desde DEVASC por RESTCONF.
