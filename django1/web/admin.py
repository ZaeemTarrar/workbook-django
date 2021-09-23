from django.contrib import admin


"""
Project Database Models
"""
from .models.referer import Referer


"""
Project Admin Boards
"""
from .admins.referer import RefererAdmin


"""
Referer Modal Registration
"""

admin.site.register(Referer, RefererAdmin)
