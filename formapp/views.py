from django.conf import settings
from django.shortcuts import render

from .forms import ContactForm
from .storage import save_submission


def home(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            save_submission(settings.SUBMISSIONS_FILE, form.cleaned_data)
            form = ContactForm()
            success = True
    else:
        form = ContactForm()

    return render(request, "formapp/home.html", {"form": form, "success": success})
