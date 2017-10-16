from django.conf import settings
from django.shortcuts import render, redirect
from django.core import mail
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from ..forms import ContactForm
from ..models import TextContact


def view_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            sender = '%s <%s>' % (
                data['contact_name'],
                data['contact_email'] or settings.EMAIL_CONTACT_FALLBACK_SENDER
            )
            mail.send_mail(
                _('contact-form-subject'),
                render_to_string('mail/contact-form.txt', data),
                sender,
                [settings.EMAIL_MANAGER],
            )
            return redirect('%s?odeslano' % reverse('contact'))
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'sent': 'odeslano' in request.GET,
        'texts': TextContact.objects.get_visible(),
    })
