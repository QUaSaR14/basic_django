from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactModelForm
from .models import Contact
import datetime

def contact(request):
    # get the form model
    form = ContactModelForm()

    # process the ajax request
    if request.is_ajax():
        form = ContactModelForm(request.POST)
        print(request.POST)

        # basic form validation
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'contact.html', {'form': form})

def messages(request):
    msgs = Contact.objects.all().order_by('-created_at')
    return render(request, 'messages.html', { 'msgs' : msgs })