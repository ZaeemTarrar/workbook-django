from django.conf.urls import url
from web.controllers.base import BaseController
from web.controllers.referer import RefererController
from web.controllers.visitor import VisitorController
from web.controllers.report import ReportController
from web.controllers.authentication import AuthenticationController as AuthController

web_routes = [
    url(r'^login', AuthController.login, name="authentication.login"),
    url(r'^visitor/registration', VisitorController.registration, name="visitor.registration"),
    url(r'^visitor/attendance', VisitorController.attendance, name="visitor.attendance"),
    url(r'^referer/registration', RefererController.registration, name="referer.registration"),
    url(r'^referer/details', RefererController.details, name="referer.details"),
    url(r'^reports', ReportController.index, name="reports.index"),
    url(r'^not-found', BaseController.not_found, name="not_found"),
    url(r'^$', BaseController.index, name="index"),
    url(r'^', BaseController.not_found, name="extra"),
]