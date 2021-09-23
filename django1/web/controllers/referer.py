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


class RefererController:

    @staticmethod
    @ApiTools.web_method_list_wrapper([ApiMethod.GET, ApiMethod.POST], ViewLinks.SimpleBootstrap.REFERER_REGISTRATION)
    def registration(request):
        def Get(req):
            return render(request, ViewLinks.SimpleBootstrap.REFERER_REGISTRATION)

        def Post(req):
            body = ApiTools.parse_body(req, True)
            error_found, msgs = validate_body_parts(body, FormValidateAbles.REFERER_ATTRIBUTES)
            data = None
            if error_found:
                new_referer = RefererModel(
                    firstname=body['first_name'],
                    middlename=body['middle_name'],
                    lastname=body['last_name'],
                    cnic=body['cnic'],
                    address=body['address'],
                    designation=body['designation'],
                    snap=body['snap_url'],
                )
                creation = new_referer.save()
                data = {"creation": creation}
            context = {
                "message": msgs if not error_found else ViewAlertMessages.RefererHandler.CREATED,
                "data": data
            }
            return render(request, ViewLinks.SimpleBootstrap.REFERER_REGISTRATION, context=context)

        tree = ApiTools.method_tree(request, get=Get, post=Post)
        del Get, Post
        return tree

    @staticmethod
    def details(request):
        return render(request, ViewLinks.SimpleBootstrap.REFERER_DETAILS)
