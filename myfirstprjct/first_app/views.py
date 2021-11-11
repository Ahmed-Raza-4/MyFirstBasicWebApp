from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,Webpage
# Create your views here.




def project(request):
    my_dict={'insert_me':''}
    return render(request,'first_app/PROJECT.html',context=my_dict)

def index(request):
    my_dict2={'insert_me2':''}
    return render(request,'first_app/index.html',context=my_dict2)

def accrec(request):
    Webpages_list = AccessRecord.objects.order_by('date')
    date_dict={'access_records': Webpages_list}
    return render(request,'first_app/accrec.html',context=date_dict)
