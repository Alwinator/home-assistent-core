"""Config flow for spotify-connector."""

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN


async def _async_has_devices(hass: HomeAssistant) -> bool:
    """Return if there are devices that can be discovered."""
    return True


config_entry_flow.register_discovery_flow(
    DOMAIN, "spotify-connector", _async_has_devices
)
