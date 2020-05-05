from django.contrib import admin
from .models import (User, ActivityPeriod,)

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display =('id','emp_id','name','timezone')


@admin.register(ActivityPeriod)
class ActivityPeriodAdmin(admin.ModelAdmin):
  list_display =('id','starttime','endtime','user_id')