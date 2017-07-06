from django.http import HttpResponse
from .models import Albume

def index(request):
    all_albumes=Albume.objects.all()
    html=''
    for albume in all_albumes:
        url='/music/'+str(albume.id)+'/'
        html+='<a href="'+url+'">'+albume.albume_title+'</a><br>'
    return HttpResponse(html)

def detail(request,albume_id):
    return HttpResponse("<h2>Detail for Albume id : "+str(albume_id)+"</h2>")
