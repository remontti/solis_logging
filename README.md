# solis_logging
Inversor Solis - Solis Data Logging Stick

Envie a pasta solis_logging para /config/custom_components/

Edite /config/configuration.yaml
```
solis_logging:
  name: Solis Data Power
  ip_address: 192.168.97.2
  username: admin
  password: admin
  timeout: 10
  retries: 1
  interval: 30
```
Default Confs:
```
DEFAULT NAME = "Solis Data Power"
DEFAULT TIMEOUT = 10
DEFAULT RETRIES = 2
DEFAULT INTERVAL = 60
DEFAULT IP_ADDRESS = "192.168.1.20"
DEFAULT USERNAME = "admin"
DEFAULT PASSWORD = "admin"
```

Reinicie seu Home Assistant
