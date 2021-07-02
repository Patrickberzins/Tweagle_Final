from django.apps import AppConfig
from django.apps import apps

def my_migration_operation(apps, schema_editor):
    Post = apps.get_model('tweagleBoard', 'Post')


class RegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registration'
