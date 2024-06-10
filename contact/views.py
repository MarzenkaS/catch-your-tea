from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponse

# Create your views here


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return HttpResponse('<h1>Thanks For Contact Us</h1>')
            # return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
