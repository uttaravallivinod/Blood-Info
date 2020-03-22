import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','BMS.settings')
import django
django.setup()
from Binfo.models import *

from faker import Faker
from random import *
f=Faker()
def phone():
    n=randint(7,9)
    num=str(n)
    for i in range(9):
        num+=str(randint(0,9))
    return num
def city():
    l=['vizag','vijianagaram','hyderabad','rajamandri','chirala','srikakulam']
    return choice(l)
def group():
    l=['A-','A+','B-','B+','O-','O+','AB-','AB+']
    return choice(l)
def gen(n):
    for i in range(n):
        fname=f.first_name()
        lname=f.last_name()
        ccity=city()
        ggroup=group()
        dob=f.date()
        pphone=phone()

        rec=Blood.objects.get_or_create(First_Name=fname,Last_Name=lname,DOB=dob,BloodGroup=ggroup,Phone=pphone,City=ccity)
gen(int(input()))
