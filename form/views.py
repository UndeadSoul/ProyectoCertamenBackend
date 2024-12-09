from django.shortcuts import render,redirect
from.forms import contactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form=contactForm()

    if request.method == "POST":
        contact_form = contactForm(data=request.POST)
        if contact_form.is_valid():
            #se está enviando el formulario
            name=request.POST.get("name","")
            email=request.POST.get("email","")
            subject=request.POST.get("subject","")
            message=request.POST.get("message","")
            #enviar el correo
            email=EmailMessage(
                "Mensaje de contacto - {}".format(subject),
                "Mensaje enviado por {} <{}>:\n\n{}".format(name,email,message),
                email,
                ["c986c7998ae9f6@inbox.mailtrap.io",],
                reply_to=[email],
            )
            try:
                email.send()
                return redirect(reverse("contact")+"?ok")
            except:
                return redirect(reverse("contact")+"?error")


    return render(request,"form/contact.html",{
        "form":contact_form,
    })