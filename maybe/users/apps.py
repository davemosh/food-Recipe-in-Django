from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

#here it import the user automatic profile making after registration
    def ready(self):
        import users.signals

