from django.apps import AppConfig


class TestApp(AppConfig):
    name = 'testapp'

    def ready(self):
        from django.contrib.admin import site as default_admin_site
        default_admin_site.enable_nav_sidebar = False
