"""Support for Solis Logging sensors."""
import logging

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import POWER_WATT
from homeassistant.helpers.entity import Entity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Solis Logging sensor platform."""
    name = hass.data[DOMAIN].get("name")
    ip_address = hass.data[DOMAIN].get("ip_address")
    username = hass.data[DOMAIN].get("username")
    password = hass.data[DOMAIN].get("password")
    timeout = hass.data[DOMAIN].get("timeout")
    retries = hass.data[DOMAIN].get("retries")
    interval = hass.data[DOMAIN].get("interval")

    async_add_entities([SolisDataPowerSensor(name, ip_address, username, password, timeout, retries, interval)], True)

class SolisDataPowerSensor(Entity):
    """Implementation of a Solis Logging sensor."""

    def __init__(self, name, ip_address, username, password, timeout, retries, interval):
        """Initialize the Solis Logging sensor."""
        self._name = name
        self._ip_address = ip_address
        self._username = username
        self._password = password
        self._timeout = timeout
        self._retries = retries
        self._interval = interval
        self._state = None

    async def async_update(self):
        """Fetch the latest data from the Solis Data Logging Stick."""
        import aiohttp

        url = f"http://{self._ip_address}/status.html"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, auth=aiohttp.BasicAuth(self._username, self._password), timeout=self._timeout) as response:
                    if response.status == 200:
                        data = await response.text()
                        start_index = data.find("var webdata_now_p")
                        end_index = data.find(";", start_index)
                        value_str = data[start_index:end_index]
                        self._state = int(value_str.split("=")[1].strip(' "'))
                    else:
                        _LOGGER.warning("Failed to fetch data from Solis Data Logging Stick. Status code: %d", response.status)
                        self._state = None

        except (aiohttp.ClientError, aiohttp.ServerConnectionError, aiohttp.ClientConnectorError) as ex:
#            _LOGGER.error("Error fetching data from Solis Data Logging Stick: %s", ex)
            self._state = 0
        except asyncio.TimeoutError as ex:
#            _LOGGER.error("Timeout error fetching data from Solis Data Logging Stick: %s", ex)
            self._state = 0

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of the sensor."""
        return POWER_WATT

