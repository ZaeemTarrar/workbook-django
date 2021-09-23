from django.shortcuts import render
from shared.structures.api_method import ApiMethod
from libs.ApiTools.__main__ import ApiTools
from utils.json_helper.__main__ import json_stringify

# Db Models
from web.models.referer import Referer as RefererModel


class BaseController:

    @staticmethod
    def index(request):
        response = redirect('/reports')
        return response

    @staticmethod
    def not_found(request):
        return render(request, ViewLinks.SimpleBootstrap.NOT_FOUND)
