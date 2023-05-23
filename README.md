# solis_logging
### Inversor - Solis Data Logging Stick

Envie a pasta <b>solis_logging</b> para <b>/config/custom_components/</b>

Edite <b>/config/configuration.yaml</b>
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
