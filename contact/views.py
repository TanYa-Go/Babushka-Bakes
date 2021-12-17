from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm



def contact(request):
    """ A view that renders the contact page"""
    submitted = False
    form = ContactForm
    

    if request.method == 'POST':
        form = ContactForm(request.POST)
        from_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        if form.is_valid():
            form.save()
            send_mail(subject, message, from_email, ['tanja.godinic@gmail.com'],)
            return HttpResponseRedirect('/contact?submitted=True')

    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True
        context = {
            'form': form,
            'submitted': submitted}
    return render(request, 'contact/contact.html', context)
