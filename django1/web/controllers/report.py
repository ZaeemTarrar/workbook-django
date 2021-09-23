from django.shortcuts import render
from shared.structures.api_method import ApiMethod
from libs.ApiTools.__main__ import ApiTools
from utils.json_helper.__main__ import json_stringify
from utils.validator.__main__ import validate_body_parts, object_has_attr
from shared.links.views import ViewLinks
from shared.structures.api_method import ApiMethod
from shared.validations.forms import FormValidateAbles
from shared.messages.view_alert_messages import ViewAlertMessages

# Db Models
from web.models.referer import Referer as RefererModel


class ReportController:

    @staticmethod
    def index(request):
        return render(request, ViewLinks.SimpleBootstrap.REPORTS)
