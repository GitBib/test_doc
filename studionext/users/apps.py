from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "studionext.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import studionext.users.signals  # noqa F401
        except ImportError:
            pass
