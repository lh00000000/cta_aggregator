from django.shortcuts import render
from api.models import Action
from django.http import HttpResponseNotFound, JsonResponse, HttpResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json


def _as_json(query_set):
    return JsonResponse(list(map(model_to_dict, query_set)))


def api_key_valid(api_key):
    # TODO - real authentication method
    return api_key == "SUPER_SECURE_KEY"


@csrf_exempt
def create(request):
    payload = json.loads(str(request.body, 'UTF-8'))
    if request.method != 'POST':
        return HttpResponse("Use POST to create new action", status=405)
    elif 'API_KEY' not in payload:
        return HttpResponse("No key", status=401)
    elif "ACTION" not in payload:
        return HttpResponse("No Action doc", status=401)
    elif not api_key_valid(payload['API_KEY']):
        return HttpResponse("Invalid key", status=403)
    elif not Action.valid_payload(payload["ACTION"]):
        return HttpResponse("Malformed doc", status=400)
    else:
        return JsonResponse(model_to_dict(Action.objects.create(**payload['ACTION'])))


def get_ical(request, event_uid):
    try:
        # TODO : need ical serializer / response?
        return Action.objects.get(event_uid=event_uid)
    except ObjectDoesNotExist:
        return HttpResponseNotFound


def getMany(request,
            filter_action_types=[
                Action.ACTION_TYPE_PHONE, Action.ACTION_TYPE_EVENT],
            future_only=False):

    if future_only:
        after = datetime.now()
    else:
        after = datetime.min

    actions = (Action.objects
               .filter(action_types__in=filter_action_types)
               .filter(end_time__gte=after))
    return JsonResponse(list(map(model_to_dict, actions)))


def getOrPost_uuid(request, event_uid):
    if request.method == 'GET':
        try:
            return JsonResponse(model_to_dict(Action.objects.get(event_uid=event_uid)))
        except ObjectDoesNotExist:
            return HttpResponseNotFound
    elif request.method in ['POST', 'PUT']:
        action, created = Action.objects.update_or_create(
            event_uid=event_uid, **request.body)
        return _as_json([action])
