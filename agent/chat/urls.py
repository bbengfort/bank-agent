from chat import views

from django.urls import path

urlpatterns = [
    path("", views.ChatUI.as_view(), name="chat-ui"),
    path("prompt", views.Prompt.as_view(), name="prompt"),
]
