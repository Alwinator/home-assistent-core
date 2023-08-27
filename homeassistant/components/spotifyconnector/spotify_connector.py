"""Includes all the querying logic of spotify connect."""


class SpotifyConnector:
    """Helper class to query and parse spotify connect."""

    def __init__(self):
        """Initialize the SpotifyConnector."""
        self.song = None
        self.user_connected = False

    def update(self):
        """Updates the data."""
        # Get logs and update class variables
        return self
