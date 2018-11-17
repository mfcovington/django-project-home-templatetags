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


@register.simple_tag
def project_home_url():
    url = home_url()
    if url:
        return url
    else:
        return ''


@register.simple_tag
def project_home_breadcrumb_bs3(label):
    if home_namespace:
        url = home_url()
        if url:
            return format_html(
                '<li><a href="{}">{}</a></li>', url, label)
        else:
            return format_html('<li>{}</li>', label)
    else:
        return ''


@register.simple_tag
def project_home_breadcrumb_bs4(label):
    if home_namespace:
        url = home_url()
        if url:
            return format_html(
                '<li class="breadcrumb-item" aria-label="breadcrumb"><a href="{}">{}</a></li>',
                url, label)
        else:
            return format_html(
                '<li class="breadcrumb-item" aria-label="breadcrumb">{}</li>',
                label)
    else:
        return ''
