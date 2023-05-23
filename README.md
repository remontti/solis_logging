# solis_logging
### Inversor - Solis Data Logging Stick

Capturando infomações via LAN, ao configurar o Data Log na rede é possivel acessar via HTTP qual fornece o valor da geração com atualizações de ~1min o que gera uma coleta/gráfico para HA mais exata.

Basta enviar a pasta <b>solis_logging</b> para <b>/config/custom_components/</b>

Edite <b>/config/configuration.yaml</b> informado os dados corretos do seu Data Logging.
```
solis_logging:
  name: Solis Data Power
  ip_address: 192.168.97.2 
  username: admin
  password: admin
  timeout: 10
  retries: 2
  interval: 60
```
Default Confs:
```
NAME = "Solis Data Power"
TIMEOUT = 10
RETRIES = 2
INTERVAL = 60
IP_ADDRESS = "192.168.1.20"
USERNAME = "admin"
PASSWORD = "admin"
```

Reinicie seu Home Assistant

<img src="https://raw.githubusercontent.com/remontti/solis_logging/main/imgs/web.png">
