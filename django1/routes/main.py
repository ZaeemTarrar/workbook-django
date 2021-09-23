# Main Required Imports
from django.contrib import admin
from django.urls import path, include
from config.settings import STATIC_URL, STATIC_ROOT
from django.conf.urls.static import static
from django.conf.urls import url

from web.routes.main import web_routes

# Django Admin Panel Routes
ADMIN = path('admin/', admin.site.urls)

# Application API Routes
apis = [
    # url(r'^referer/all', RefererApi.fetch_all, name="Referer.fetch_all"),
]

# Routes Wrapping Together
urlpatterns = [
    ADMIN,
    path(r'api/', include(apis), name="Project.api.routes"),
    path(r'', include(web_routes), name="Project.web.routes"),
]