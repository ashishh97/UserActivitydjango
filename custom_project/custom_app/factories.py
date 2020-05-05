import factory
import factory.django
from .models import User, ActivityPeriod
import random
import string
import datetime
import factory.fuzzy
import pytz 

def generate_serial():
    return 'FTL' + ''.join(["%s" % random.randint(0, 9) for num in range(0, 6)])

def generate_user_id():
    qs = User.objects.all()
    # lst = []
    # for a in qs:
    #     lst.append(a.id)
    return random.choice(qs)

class UserFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = User

    emp_id = factory.fuzzy.FuzzyAttribute(generate_serial)
    name = factory.Faker('name')
    timezone = factory.Faker('timezone')

class ActivityPeriodFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = ActivityPeriod

    starttime = factory.fuzzy.FuzzyDateTime(
        datetime.datetime(2019, 1, 1, tzinfo=pytz.timezone('UTC')),
        datetime.datetime(2020, 1, 1, tzinfo=pytz.timezone('UTC')),
    )
    endtime = factory.LazyAttribute(lambda o: o.starttime + datetime.timedelta(days=7))
    user_id = factory.fuzzy.FuzzyAttribute(generate_user_id)