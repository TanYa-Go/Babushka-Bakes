from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect

def contact(request):
    """ A view that renders the contact page"""
    submitted = False
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact?submitted=True')
    else:      
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True
        context = {
            'form': form,
            'submitted': submitted}
    return render(request, 'contact/contact.html', context)
