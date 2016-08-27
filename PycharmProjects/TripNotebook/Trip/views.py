from django.shortcuts import render_to_response
from Trip.models import TripMain,Plan
from weasyprint import HTML, CSS
from django.http import HttpResponse
from django.template import RequestContext, loader, context
from django.shortcuts import render
from Trip.forms import TripMainForm, PlanForm
from django.http import HttpResponseRedirect

# Create your views here.
def indexPage(request):
    tripList = TripMain.objects.all()

    #context['loop_times'] = range(1, 8)

    return render_to_response('index2.html',locals())

def about(request):
    return render_to_response('about.html')

def trip(request):
    return render_to_response('single.html')

def tripDetails(request,pk):
    trip = TripMain.objects.get(id=pk)
    try:
        planList = trip.plan_set.all()
        planList = planList.order_by('TimeStart')
        tmp = planList[0]
        dayList = planList.order_by('dayCount').values_list('dayCount', flat=True).distinct()
        totalDay = TripMain.objects.get(id=pk).TotalDay
    except:
        print("尚未有任何行程資料！")

    return render_to_response('single.html', locals())

def codes(request):
    return render_to_response('codes.html')

def contact(request):
    return  render_to_response('contact.html')

def gallery(request):
    return render_to_response('gallery.html')

def services(request):
    return render_to_response('services.html')

def costlist(request):
    return render_to_response('costlist.html')

def presentlist(request):
    return render_to_response('presentlist.html')

def travellist(request):
    return render_to_response('travellist.html')

def fullPlan(request,pk):
    trip = TripMain.objects.get(id=pk)
    planList = trip.plan_set.all()
    planList = planList.order_by('TimeStart')
    tmp = planList[0]
    dayList = Plan.objects.order_by('dayCount').values_list('dayCount', flat=True).distinct()
    rowCountForList = 15

    return render_to_response('fullPlanPrint.html',locals())

def printPdf(request,pk):

    trip = TripMain.objects.get(id=pk)
    context_dict = {
        'planList': trip.plan_set.all(),
        'dayList' : Plan.objects.order_by('dayCount').values_list('dayCount', flat=True).distinct()
    }

    template = loader.get_template('fullPlanPrint.html')
    html = template.render(RequestContext(request, context_dict))
    response = HttpResponse(content_type='application/pdf')
    HTML(string=html).write_pdf(response,stylesheets=[CSS(string='body { font-family: Arial }')])

    return response


def test(request):
    return render(request, 'test.html')


def createTripMain(request):
    if request.method == 'POST':
        form = TripMainForm(request.POST)
        if form.is_valid():
            new_tripMain = form.save()
            return HttpResponseRedirect('/single/'+str(new_tripMain.pk))
    else:
        form = TripMainForm()
    return render(request, 'createTripMain.html',{'form': form })

def createPlan(request,pk):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit = False)
            plan.trip = TripMain.objects.get(id=pk)
            plan.save()
            return HttpResponseRedirect('/single/'+str(pk))
    else:
        form = PlanForm()
    return render(request, 'createTripMain.html',{'form': form })