from django.shortcuts import render, redirect
from django.urls import reverse
from . forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            email = EmailMessage(
                "Kyanime: Nuevo mensaje de Contacto owo",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "kyanime.mail@gmail.com",
                ["kyanime.mail@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contacto')+'?ok')
            except:
                return redirect(reverse('contacto')+'?fail')

    return render(request, "contact/contacto.html", {'form': contact_form})
