from django.views.generic import TemplateView


class ChatUI(TemplateView):

    template_name = "chat.html"
