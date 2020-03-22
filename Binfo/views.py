from django.shortcuts import render
from Binfo.forms import BloodForm
from Binfo.models import Blood
from django.core.exceptions import ValidationError
# Create your views here.
def home(request):
    return render(request,'base.html')
def display(request):
    c=Blood.objects.all()
    data=[]
    for i in c:
        data.append(i.City)
    data=set(data)
    data=list(data)
    city='city:all'
    bg='blood:all'
    if request.method=='POST':
        city=request.POST['req']
        bg=request.POST['reqbg']
        if bg=='Null':
            c=Blood.objects.all().filter(City=city)
        if city=='Null':
            c=Blood.objects.all().filter(BloodGroup=bg)
        if city!='Null' and bg!='Null':
            c=Blood.objects.all().filter(City=city,BloodGroup=bg)
        return render(request,'display.html',context={'c':c,'data':data,'city':city,'bgg':bg})

    return render(request,'display.html',context={'data':data,'c':c,'city':city,'bgg':bg})
def hh(request):

    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        dob=request.POST['dob']
        bg=request.POST['bg']
        phone=request.POST['phone']
        city=request.POST['city']
        if len(phone)!=10:
            raise ValidationError('enter correct phone number')
        form=Blood(First_Name=fname,Last_Name=lname,DOB=dob,BloodGroup=bg,Phone=phone,City=city)

        form.save()


    return render(request,'reg.html')
