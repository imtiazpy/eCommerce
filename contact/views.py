from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from contact.models import Contact


@login_required(login_url='/accounts/login')
def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            email=request.POST.get('email', ''),
            subject=request.POST.get('subject', ''),
            message=request.POST.get('message', ''),
        )
        messages.success(request, "Your message has been submitted.")
    context = {
        'contact': True
    }
    return render(request, 'contact/contact.html', context=context)
