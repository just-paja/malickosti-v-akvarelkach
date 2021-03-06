from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect
from django.core import mail
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from drawings.models import Drawing, DRAWING_AVAILABLE_STATES
from texts.models import ContactText

from ..forms import ContactForm


def view_contact(request, id=None):
    drawing = None
    if id:
        try:
            drawing = Drawing.objects.exclude(
                status__in=DRAWING_AVAILABLE_STATES,
            ).get(id=id)
        except ObjectDoesNotExist:
            raise Http404

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            sender = '%s <%s>' % (
                data['contact_name'],
                data['contact_email'] or settings.EMAIL_CONTACT_FALLBACK_SENDER
            )
            mail_result = mail.send_mail(
                _('contact-form-subject'),
                render_to_string('mail/contact-form.txt', data),
                sender,
                [settings.EMAIL_MANAGER],
            )
            redirect_path = '%s?odeslano' if mail_result else '%s?selhalo'
            return redirect(redirect_path % request.path)
    else:
        initial_data = {}
        if drawing:
            initial_data['contact_message'] = _('contact-prefill-message-redraw') % (
                drawing.name,
                drawing.size.name,
                request.build_absolute_uri(
                    reverse('drawings-detail', kwargs={'id': drawing.id})
                ),
            )
        form = ContactForm(initial=initial_data)

    return render(request, 'contact.html', {
        'form': form,
        'redraw': drawing,
        'sent': 'odeslano' in request.GET,
        'failed': 'selhalo' in request.GET,
        'texts': ContactText.objects.get_visible(),
    })
