from django import template
from django.utils.formats import date_format

register = template.Library()

FORMAT_TIME = 'G:i'

FORMAT_DATE = 'd. E Y'
FORMAT_DATE_SHORT = 'd. E'
FORMAT_DATETIME = 'd. E Y %s' % FORMAT_TIME
FORMAT_DATETIME_SHORT = 'd. E %s' % FORMAT_TIME

@register.filter(name='event_date')
def event_date(event):
    value = []
    start_format = FORMAT_DATETIME
    end_format = None

    if event.all_day:
        if (
            event.start.date().year == event.end.date().year and
            event.start.date() != event.end.date()
        ):
            start_format = FORMAT_DATE_SHORT
        else:
            start_format = FORMAT_DATE
    elif event.start.date().year == event.end.date().year:
        start_format = FORMAT_DATETIME_SHORT

    value.append(date_format(event.start, start_format))

    if event.all_day and event.start.date() != event.end.date():
        end_format = FORMAT_DATE

    if not event.all_day:
        if event.start.date() == event.end.date():
            end_format = FORMAT_TIME
        elif event.start.year == event.end.year:
            end_format = FORMAT_DATETIME
        else:
            end_format = FORMAT_DATETIME_SHORT

    if end_format:
        value.append(date_format(event.end, end_format))

    return ' - '.join(value)
