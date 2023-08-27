"""The registration of all spotify-connector binary sensors."""
import logging

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .spotify_connector import SpotifyConnector

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up rpi_power binary sensor."""
    connector = hass.data[DOMAIN][entry.entry_id]
    connector_job = await hass.async_add_executor_job(connector.update)
    async_add_entities([UserConnectedBinarySensor(connector_job)], True)


class UserConnectedBinarySensor(BinarySensorEntity):
    """Indicates if a user is connected to Spotify Connect."""

    _attr_device_class = BinarySensorDeviceClass.CONNECTIVITY
    _attr_icon = "mdi:user"
    _attr_name = "Spotify Connect User Connected"
    _attr_unique_id = "spotify_connect_user_connected"

    def __init__(self, connector: SpotifyConnector) -> None:
        """Initialize the binary sensor."""
        self.connector = connector

    def update(self) -> None:
        """Update the state."""
        self._attr_is_on = self.connector.user_connected
