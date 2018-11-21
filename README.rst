********************************
django-project-home-templatetags
********************************

``django-project-home-templatetags`` is a collection of Django templatetags to flexibly incorporate links and breadcrumbs from app pages to the homepage of a project.

If ``PROJECT_HOME_NAMESPACE`` is not defined to ``settings.py``, these template tags are silenced.

Source code is available on GitHub at `mfcovington/django-project-home-templatetags <https://github.com/mfcovington/django-project-home-templatetags>`_.

.. contents:: :local:


Installation
============

**PyPI**

.. code-block:: sh

    pip install django-project-home-templatetags


**GitHub (development branch)**

.. code-block:: sh

    pip install git+http://github.com/mfcovington/django-project-home-templatetags.git@develop


Configuration
=============

Add ``project_home_tags`` to ``INSTALLED_APPS`` in ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'project_home_tags',
    )


Specify the ``PROJECT_HOME_NAMESPACE`` in ``settings.py``:

.. code-block:: python

    PROJECT_HOME_NAMESPACE = 'project_name:index_view'


By default, a link created with a ``project_home_tags`` template tag has 'Home' as its text. This can be overridden by defining an optional project-wide label with ``PROJECT_HOME_LABEL`` in ``settings.py``:

.. code-block:: python

    PROJECT_HOME_LABEL = 'Homepage'    # Optional; Default is 'Home'


Both the default and the project-wide label can be overridden by passing a string to the template tag. For example:

.. code-block:: python

    {% project_home_breadcrumb_bs4 'Custom Label' %}


Template Tags
=============

``{% load project_home %}``
--------------------------------

Loads the project home template tags in your Django template.


``{% project_home_url %}``
--------------------------

A template tag to return the project's home URL.

.. code-block:: python

    {% load project_home %}

    <a href="{% project_home_url %}">Home</a>


If ``settings.PROJECT_HOME_NAMESPACE`` is defined as ``'project_name:index_view'``, this is equivalent to:

.. code-block:: python

    <a href="{% url 'project_name:index_view' %}">Home</a>


``{% project_home_breadcrumb_bs3 %}``
-------------------------------------

A template tag to return the project's home URL and label formatted as a `Bootstrap 3 breadcrumb <https://getbootstrap.com/docs/3.3/components/#breadcrumbs>`_.

.. code-block:: python

    {% load project_home %}

    <ol class="breadcrumb">
      {% project_home_breadcrumb_bs3 %}    {# <--- #}
      <li><a href="{% url 'app:namespace' %}">List of Objects</a></li>
      <li class="active">Object Detail</li>
    </ol>


If ``settings.PROJECT_HOME_NAMESPACE`` is defined as ``'project_name:index_view'``, this is equivalent to:

.. code-block:: python

    <ol class="breadcrumb">
      <li><a href="{% url 'project_name:index_view' %}">Home</a></li>    {# <--- #}
      <li><a href="{% url 'app:namespace' %}">List of Objects</a></li>
      <li class="active">Object Detail</li>
    </ol>


``{% project_home_breadcrumb_bs4 %}``
-------------------------------------

A template tag to return the project's home URL and label formatted as a `Bootstrap 4 breadcrumb <https://getbootstrap.com/docs/4.1/components/breadcrumb/>`_.

.. code-block:: python

        {% load project_home %}

        <ol class="breadcrumb">
          {% project_home_breadcrumb_bs4 %}    {# <--- #}
          <li class="breadcrumb-item" aria-label="breadcrumb"><a href="{% url 'app:namespace' %}">List of Objects</a></li>
          <li class=" breadcrumb-item active" aria-label="breadcrumb" aria-current="page">Object Detail</li>
        </ol>


If ``settings.PROJECT_HOME_NAMESPACE`` is defined as ``'project_name:index_view'``, this is equivalent to:

.. code-block:: python

        <ol class="breadcrumb">
          <li class="breadcrumb-item" aria-label="breadcrumb"><a href="{% url 'project_name:index_view' %}">Home</a></li>    {# <--- #}
          <li class="breadcrumb-item" aria-label="breadcrumb"><a href="{% url 'app:namespace' %}">List of Objects</a></li>
          <li class=" breadcrumb-item active" aria-label="breadcrumb" aria-current="page">Object Detail</li>
        </ol>


*Version 0.0.0*
