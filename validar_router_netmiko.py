from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "IP_DEL_CSR",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}

conexion = ConnectHandler(**router)
conexion.enable()

comandos = [
    "show ip interface brief",
    "show running-config",
    "show version",
]

for comando in comandos:
    print("=" * 80)
    print(f"Comando ejecutado: {comando}")
    print("=" * 80)
    print(conexion.send_command(comando))
    print()

conexion.disconnect()
