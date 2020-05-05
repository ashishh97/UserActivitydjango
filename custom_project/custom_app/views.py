from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, combinedSerializer, ActivityPeriodSerializer
from .models import User, ActivityPeriod
from collections import namedtuple
import copy
Timeline = namedtuple('Timeline', ('user', 'activity'))
# Create your views here.
class ActivityView(APIView):
  def get(self, request, *args, **kwargs):
    qs = User.objects.all()
    
    final_dic = {}
    final_lst = []
    for a in qs:
      new_dic = {}
      new_dic['id'] = a.emp_id
      new_dic['real_name'] = a.name
      new_dic['tz'] = a.timezone
      activity_id = ActivityPeriod.objects.filter(user_id=a.id)
      temp_lst = []
      for b in activity_id:
        temp_dic = {}
        string_time = b.starttime.strftime("%b %d %Y %I:%M%p")
        temp_dic['start_time'] = string_time
        end_string_time = b.endtime.strftime("%b %d %Y %I:%M%p")
        temp_dic['end_time'] = end_string_time
        temp_lst.append(temp_dic)
      new_dic['activity_period'] = temp_lst
      final_lst.append(new_dic)
    final_dic['ok'] = True
    final_dic['member'] = final_lst
    # serializer = ActivityPeriodSerializer(activity_id,many=True)
    return JsonResponse(final_dic)
