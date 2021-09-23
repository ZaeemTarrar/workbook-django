import json
import sys
from urllib.parse import parse_qs
from webbrowser import Error

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from shared.structures.alert_message import AlertMessage
from shared.structures.api_method import ApiMethod
from shared.structures.http_status import HttpStatus
from shared.messages.api_responses import ApiResponseMessages as ARM
from shared.links.views import ViewLinks


class ApiTools:

    @staticmethod
    def method_tree(request, get=None, post=None, put=None, patch=None, delete=None):
        if request.method == ApiMethod.GET and get:
            return get(request)
        elif request.method == ApiMethod.POST and post:
            return post(request)
        elif request.method == ApiMethod.PUT and put:
            return put(request)
        elif request.method == ApiMethod.PATCH and patch:
            return patch(request)
        elif request.method == ApiMethod.DELETE and delete:
            return delete(request)
        else:
            return get(request)

    @staticmethod
    def parse_body(request, multi=None):
        parsed_body = dict(parse_qs(request.body.decode('utf-8')))
        items = dict()
        for attr, value in parsed_body.items():
            if attr != 'csrfmiddlewaretoken':
                if multi:
                    items[attr] = value[0]
                else:
                    items[attr] = value
        return items

    @staticmethod
    def getStatusCode(code=200):
        if code == HttpStatus.OK:
            return "OK"
        elif code == HttpStatus.CREATED:
            return "CREATED"
        elif code == HttpStatus.BAD_REQUEST:
            return "BAD_REQUEST"
        elif code == HttpStatus.NOT_FOUND:
            return "NOT_FOUND"
        else:
            return "INTERNAL_SERVER_ERROR"

    @staticmethod
    def send(code=200, msg=None, data=None):
        try:
            message = {}
            if msg is not None:
                if len(msg) >= 1 and msg[0]:
                    message['text'] = msg[0] or "Anonymous"
                else:
                    message['text'] = "..."
                if len(msg) == 2 and msg[1]:
                    message['type'] = msg[1]
                else:
                    message['type'] = "SUCCESS"
            response = dict(code=200, status="OK", message={
                "text": "",
                "type": "SUCCESS"
            }, data=None)
            response['code'] = code
            response['status'] = ApiTools.getStatusCode(code)
            if message:
                response['message'] = message
            if data:
                response['data'] = data
            response_json = json.dumps(response)
            return HttpResponse(response_json, content_type="application/json")
        except TypeError:
            response = dict(code=400, status="BAD_REQUEST", message={
                "text": "TypeError",
                "type": "WARNING"
            }, data=None)
            response_json = json.dumps(response)
            return HttpResponse(response_json, content_type="application/json")

    @staticmethod
    def method_wrapper(method=ApiMethod.GET):
        print("API Method: {}".format(method))

        def inner_wrapper(wrapped_function):
            def passable_function(*args, **kwargs):
                request = args[0]

                try:
                    if request.method == method:
                        return wrapped_function(request)
                    else:
                        return ApiTools.send(
                            code=HttpStatus.BAD_REQUEST,
                            msg=[ARM.Handler.METHOD_NOT_ALLOWED, AlertMessage.WARNING]
                        )
                except TypeError:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["Type Error: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    return result
                except AttributeError as ex:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["Attribute Error: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    return result
                except AssertionError as ex:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["Assertion Error: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    return result
                except MultiValueDictKeyError as ex:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["MultiValueDictKeyError: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    return result
                except Error as ex:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["Error: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    return result
                finally:
                    pass

            return passable_function

        return inner_wrapper

    @staticmethod
    def web_method_wrapper(method=ApiMethod.GET):
        def inner_wrapper(wrapped_function):
            def passable_function(*args, **kwargs):
                request = args[0]

                try:
                    if request.method == method:
                        return wrapped_function(request)
                    else:
                        return render(request, "views/simple_bootstrap/not_found.html")
                except TypeError:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["Type Error: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    return result
                except AttributeError as ex:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["Attribute Error: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    return result
                except AssertionError as ex:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["Assertion Error: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    return result
                except MultiValueDictKeyError as ex:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["MultiValueDictKeyError: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    return result
                except Error as ex:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["Error: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    return result
                finally:
                    pass

            return passable_function

        return inner_wrapper

    @staticmethod
    def web_method_list_wrapper(method=None, Url=ViewLinks.SimpleBootstrap.NOT_FOUND):
        if method is None:
            method = [ApiMethod.GET]

        def inner_wrapper(wrapped_function):
            def passable_function(*args, **kwargs):
                request = args[0]

                try:
                    if request.method in method:
                        return wrapped_function(request)
                    else:
                        return render(request, Url, context=None)
                except AssertionError as ex:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    result = ApiTools.send(
                        code=HttpStatus.BAD_REQUEST,
                        msg=["Error: {}".format(str(ex_value)), AlertMessage.WARNING],
                    )
                    context = {
                        "message": str(ex_value)
                    }
                    return render(request, Url, context=context)
                except Error as ex:
                    ex_type, ex_value, ex_traceback = sys.exc_info()
                    context = {
                        "message": str(ex_value)
                    }
                    return render(request, Url, context=context)
                finally:
                    pass

            return passable_function

        return inner_wrapper
