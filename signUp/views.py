from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
# Create your views here.


def index(request):
    insertForm = SignUpForm(request.POST or None)

    if insertForm.is_valid():
        save = insertForm.save(commit = False)
        save = insertForm.save()
        return HttpResponseRedirect('thank-you/')
    #message
    context = {"form": insertForm}
    templates = 'signUp/index.html'
    return render(request, templates,context)

def thankyou(request):
    context = {}
    templates = 'signUp/thankyou.html'
    return render(request, templates,context)