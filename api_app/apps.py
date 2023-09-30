from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'

    # def ready(self):
    #     print('starting scheduler...')
    #     from .weather_scheduler import weather_updater
    #     weather_updater.start()
