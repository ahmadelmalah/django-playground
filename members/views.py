from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def index(request):
    members = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))