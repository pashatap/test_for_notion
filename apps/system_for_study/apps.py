from django.apps import AppConfig


class SystemForStudyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.system_for_study'

    def ready(self):
        pass
