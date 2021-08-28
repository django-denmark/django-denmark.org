"""djangodenmark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django_consent import urls as consent_urls

from .apps.companies import urls as company_urls
from .apps.events import urls as event_urls
from .apps.jobposts import urls as jobpost_urls
from .apps.newsletter import urls as newsletter_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(event_urls)),
    path("accounts/", include("djangodenmark.apps.accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("companies/", include(company_urls)),
    path("jobs/", include(jobpost_urls)),
    path("consent/", include(consent_urls)),
    path("newsletter/", include(newsletter_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # conditionally adding django-debug-toolbar URLs
    # make sure to include in INSTALLED_APPS + MIDDLEWARE + INTERNAL_IPS are set
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
