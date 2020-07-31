from django.shortcuts import render
from myblog.models import SiteInfo
# Create your views here.
def index(request):
    print('开始读取数据')
    siteinfo = SiteInfo.objects.all()[0]
    print(siteinfo.title)
    print(siteinfo.logo) 

    data = {
        "siteinfo":siteinfo
    }
    return render(request,'index.html',data)
