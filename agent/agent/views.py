from django.shortcuts import redirect


def landing(request):
    if request.user.is_authenticated:
        return redirect("chat-ui")
    else:
        return redirect("login")
