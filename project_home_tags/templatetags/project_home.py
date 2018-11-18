from functools import wraps

from django import template
from django.conf import settings
from django.urls import reverse
from django.utils.html import format_html


register = template.Library()
home_namespace = getattr(settings, 'PROJECT_HOME_NAMESPACE', None)

def home_url():
    try:
        return reverse(home_namespace)
    except Exception:
        return None


def silence_without_namespace(f):
    @wraps(f)
    def wrapped(label=None):
        if not home_namespace:
            return ''
        if label:
            return f(label)
        else:
            return f()
    return wrapped


@register.simple_tag
@silence_without_namespace
def project_home_url(*args):
    url = home_url()
    if url:
        return url


@register.simple_tag
@silence_without_namespace
def project_home_breadcrumb_bs3(label):
    url = home_url()
    if url:
        return format_html(
            '<li><a href="{}">{}</a></li>', url, label)
    else:
        return format_html('<li>{}</li>', label)


@register.simple_tag
@silence_without_namespace
def project_home_breadcrumb_bs4(label):
    url = home_url()
    if url:
        return format_html(
            '<li class="breadcrumb-item" aria-label="breadcrumb"><a href="{}">{}</a></li>',
            url, label)
    else:
        return format_html(
            '<li class="breadcrumb-item" aria-label="breadcrumb">{}</li>',
            label)
