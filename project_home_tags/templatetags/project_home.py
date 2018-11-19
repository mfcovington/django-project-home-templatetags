from functools import wraps

from django import template
from django.conf import settings
from django.urls import reverse
from django.utils.html import format_html


register = template.Library()
home_namespace = getattr(settings, 'PROJECT_HOME_NAMESPACE', None)
home_label = getattr(settings, 'PROJECT_HOME_LABEL', 'Home')

def home_url():
    """Get project's home URL based on settings.PROJECT_HOME_NAMESPACE.

    Returns None if PROJECT_HOME_NAMESPACE is not defined in settings.
    """
    try:
        return reverse(home_namespace)
    except Exception:
        return None


def silence_without_namespace(f):
    """Decorator to silence template tags if 'PROJECT_HOME_NAMESPACE' is
    not defined in settings.

    Usage Example:
        from django import template


        register = template.Library()

        @register.simple_tag
        @silence_without_namespace
        def a_template_tag(*args):
            ...
    """
    @wraps(f)
    def wrapped(label=None):
        if not home_namespace:
            return ''
        if label:
            return f(label)
        else:
            return f(home_label)
    return wrapped


@register.simple_tag
@silence_without_namespace
def project_home_url(*args):
    """A template tag to return the project's home URL.

    PROJECT_HOME_NAMESPACE must be defined in settings.
    For example:
        PROJECT_HOME_NAMESPACE = 'project_name:index_view'

    Usage Example:
        {% load project_home_tags %}

        <a href="{% project_home_url %}">Home</a>
    """
    url = home_url()
    if url:
        return url


@register.simple_tag
@silence_without_namespace
def project_home_breadcrumb_bs3(label):
    """A template tag to return the project's home URL and label
    formatted as a Bootstrap 3 breadcrumb.

    PROJECT_HOME_NAMESPACE must be defined in settings, for example:
        PROJECT_HOME_NAMESPACE = 'project_name:index_view'

    Usage Example:
        {% load project_home_tags %}

        <ol class="breadcrumb">
          {% project_home_breadcrumb_bs3 %}    {# <--- #}
          <li><a href="{% url 'app:namespace' %}">List of Objects</a></li>
          <li class="active">Object Detail</li>
        </ol>

    This gets converted into:
        <ol class="breadcrumb">
          <li><a href="{% url 'project_name:index_view' %}">Home</a></li>    {# <--- #}
          <li><a href="{% url 'app:namespace' %}">List of Objects</a></li>
          <li class="active">Object Detail</li>
        </ol>

    By default, the link's text is 'Home'. A project-wide label can be
    defined with PROJECT_HOME_LABEL in settings. Both the default and
    the project-wide label can be overridden by passing a string to
    the template tag.

    For example:
        {% project_home_breadcrumb_bs3 'Custom Label' %}
    """
    url = home_url()
    if url:
        return format_html(
            '<li><a href="{}">{}</a></li>', url, label)
    else:
        return format_html('<li>{}</li>', label)


@register.simple_tag
@silence_without_namespace
def project_home_breadcrumb_bs4(label):
    """A template tag to return the project's home URL and label
    formatted as a Bootstrap 4 breadcrumb.

    PROJECT_HOME_NAMESPACE must be defined in settings, for example:
        PROJECT_HOME_NAMESPACE = 'project_name:index_view'

    Usage Example:
        {% load project_home_tags %}

        <ol class="breadcrumb">
          {% project_home_breadcrumb_bs4 %}    {# <--- #}
          <li class="breadcrumb-item" aria-label="breadcrumb"><a href="{% url 'app:namespace' %}">List of Objects</a></li>
          <li class=" breadcrumb-item active" aria-label="breadcrumb" aria-current="page">Object Detail</li>
        </ol>

    This gets converted into:
        <ol class="breadcrumb">
          <li class="breadcrumb-item" aria-label="breadcrumb"><a href="{% url 'project_name:index_view' %}">Home</a></li>    {# <--- #}
          <li class="breadcrumb-item" aria-label="breadcrumb"><a href="{% url 'app:namespace' %}">List of Objects</a></li>
          <li class=" breadcrumb-item active" aria-label="breadcrumb" aria-current="page">Object Detail</li>
        </ol>

    By default, the link's text is 'Home'. A project-wide label can be
    defined with PROJECT_HOME_LABEL in settings. Both the default and
    the project-wide label can be overridden by passing a string to
    the template tag.

    For example:
        {% project_home_breadcrumb_bs4 'Custom Label' %}
    """
    url = home_url()
    if url:
        return format_html(
            '<li class="breadcrumb-item" aria-label="breadcrumb"><a href="{}">{}</a></li>',
            url, label)
    else:
        return format_html(
            '<li class="breadcrumb-item" aria-label="breadcrumb">{}</li>',
            label)
