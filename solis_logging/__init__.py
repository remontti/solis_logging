"""The Solis Logging integration."""
import logging

import voluptuous as vol

from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.discovery import load_platform
from homeassistant.helpers.typing import HomeAssistantType, ConfigType

from .const import DOMAIN, DEFAULT_NAME, DEFAULT_IP_ADDRESS, DEFAULT_USERNAME, DEFAULT_PASSWORD, DEFAULT_TIMEOUT, DEFAULT_RETRIES, DEFAULT_INTERVAL

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
                vol.Optional("ip_address", default=DEFAULT_IP_ADDRESS): cv.string,
                vol.Optional("username", default=DEFAULT_USERNAME): cv.string,
                vol.Optional("password", default=DEFAULT_PASSWORD): cv.string,
                vol.Optional("timeout", default=DEFAULT_TIMEOUT): int,
                vol.Optional("retries", default=DEFAULT_RETRIES): int,
                vol.Optional("interval", default=DEFAULT_INTERVAL): int,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

def setup(hass: HomeAssistantType, config: ConfigType) -> bool:
    """Set up the Solis Logging component."""
    conf = config.get(DOMAIN)

    if conf is None:
        conf = {}

    name = conf.get(CONF_NAME, DEFAULT_NAME)
    ip_address = conf.get("ip_address", DEFAULT_IP_ADDRESS)
    username = conf.get("username", DEFAULT_USERNAME)
    password = conf.get("password", DEFAULT_PASSWORD)
    timeout = conf.get("timeout", DEFAULT_TIMEOUT)
    retries = conf.get("retries", DEFAULT_RETRIES)
    interval = conf.get("interval", DEFAULT_INTERVAL)

    hass.data[DOMAIN] = {
        CONF_NAME: name,
        "ip_address": ip_address,
        "username": username,
        "password": password,
        "timeout": timeout,
        "retries": retries,
        "interval": interval,
    }

    load_platform(hass, "sensor", DOMAIN, {}, config)

    return True

