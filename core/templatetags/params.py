import calendar
import datetime
from django import template
from django.http import QueryDict
from core.models import Bookmark
from time import time
from django import template

register = template.Library()


@register.simple_tag
def relative_url(
    param_key: str,
    param_value: str,
    querydict: QueryDict = None
) -> str:
    """
    Construct and return a query params string.
    Arguments passed to this function take
    precedence over any existing query param
    for a request.
    """
    # QueryDicts are immutable by default.
    new_querydict = QueryDict(mutable=True)
    new_querydict.appendlist(param_key, param_value)
    """ for key, value in new_querydict.items():
        if key == param_key:
            new_querydict.pop(key) """
    if not querydict:
        # No existing query params in the URL, so we're done.
        # We just needed to append the args that were
        # passed to this function.
        return f"?{new_querydict.urlencode()}"
    else:
        """
            Removes a param if unchecked in template
        """
        for key, value in querydict.items():
            if key == param_key and new_querydict[key] != value:
                new_querydict[key] = value
                continue
            if key == param_key:
                new_querydict.pop(key)
                

        # This means there are some existing params in the URL.
        # We'd like to append them now and return that URL.
        # At the same time, we want to ensure that the
        # param_key and param_value passed to the function
        # take precedence over the one in the URL.
        # That happens when we check for key != param_key.
        for key, value in querydict.items():
            if key != param_key:
                new_querydict.appendlist(key, value)
        
        #print(new_querydict)
        return f"?{new_querydict.urlencode()}"


TIMESINCE_CHUNKS = (
    (60 * 60 * 24 * 365, '%d year'),
    (60 * 60 * 24 * 30, '%d month'),
    (60 * 60 * 24 * 7, '%d week'),
    (60 * 60 * 24, '%d day'),
    (60 * 60, '%d hour'),
    (60, '%d minute')
)


def time_since(d, now=None, reversed=False):
    """
    Takes two datetime objects and returns the time between d and now
    as a nicely formatted string, e.g. "10 minutes".  If d occurs after now,
    then "0 minutes" is returned.
    Units used are years, months, weeks, days, hours, and minutes.
    Seconds and microseconds are ignored.  Up to two adjacent units will be
    displayed.  For example, "2 weeks, 3 days" and "1 year, 3 months" are
    possible outputs, but "2 weeks, 3 hours" and "1 year, 5 days" are not.
    Adapted from
    http://web.archive.org/web/20060617175230/http://blog.natbat.co.uk/archive/2003/Jun/14/time_since
    """
    # Convert datetime.date to datetime.datetime for comparison.
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    if now and not isinstance(now, datetime.datetime):
        now = datetime.datetime(now.year, now.month, now.day)

    if not now:
        now = datetime.datetime.now()

    delta = (now.replace(tzinfo=None) - d.replace(tzinfo=None))

    # Deal with leapyears by subtracing the number of leapdays
    delta -= datetime.timedelta(calendar.leapdays(d.year, now.year))

    # ignore microseconds
    since = delta.days * 24 * 60 * 60 + delta.seconds
    if since <= 0:
        # d is in the future compared to now, stop processing.
        return '0 minutes'
    for i, (seconds, name) in enumerate(TIMESINCE_CHUNKS):
        count = since // seconds
        if count != 0:
            break

    result = name % count
    return result


register.filter('time_since', time_since)
