from __future__ import unicode_literals

from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = 'backend'

    def ready(self):
        """
        Import the signals
        """
        import backend.signals
