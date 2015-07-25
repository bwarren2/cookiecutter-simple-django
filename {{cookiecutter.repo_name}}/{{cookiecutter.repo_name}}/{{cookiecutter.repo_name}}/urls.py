from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import BootstrapView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^styles/$', BootstrapView.as_view(), name='bootstrap_test'),

)
