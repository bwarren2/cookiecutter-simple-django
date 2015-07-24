from django.views.generic import TemplateView


class BootstrapView(TemplateView):
    template_name = 'blog/bootstrap_test.html'
