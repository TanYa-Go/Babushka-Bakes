from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm


def contact(request):
    """ A view that renders the contact page"""
    submitted = False
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST['name']
        from_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        html_email = render_to_string(
                'emails/contact_form_template.html', {'name': name, 'from_email': from_email, 'subject': subject, 'message': message})
        if form.is_valid():
            form.save()
            send_mail(
                subject, message, from_email, ['tanja.godinic@gmail.com'], html_message=html_email, fail_silently=False)
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True
        context = {
            'form': form,
            'submitted': submitted}
    return render(request, 'contact/contact.html', context)
