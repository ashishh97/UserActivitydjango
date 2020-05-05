from rest_framework import serializers
from .models import User,ActivityPeriod

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields =('emp_id','name','timezone')

class ActivityPeriodSerializer(serializers.ModelSerializer):
  emp_id = serializers.ReadOnlyField(source = 'user_id.emp_id')
  name = serializers.ReadOnlyField(source = 'user_id.name')
  timezone = serializers.ReadOnlyField(source = 'user_id.timezone')
  class Meta:
    model = ActivityPeriod
    fields =('emp_id','name','timezone','starttime','endtime')

class combinedSerializer(serializers.Serializer):
  user = UserSerializer(many=True)
  activity = ActivityPeriodSerializer(many=True)