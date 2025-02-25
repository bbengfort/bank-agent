from django.apps import AppConfig


class ChatConfig(AppConfig):

    default_auto_field = "django.db.models.BigAutoField"
    name = "chat"

    def ready(self):
        import vertexai
        from django.conf import settings

        vertexai.init(
            project=settings.GOOGLE_CLOUD_PROJECT,
            location=settings.GOOGLE_CLOUD_LOCATION,
        )
