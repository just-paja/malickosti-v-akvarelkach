from django.shortcuts import render

from texts.models import ConditionsText


def view_conditions(request):
    return render(request, 'conditions.html', {
        'conditions': ConditionsText.objects.get_visible(),
    })
