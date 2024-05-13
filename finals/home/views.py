from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .filters import FilterCourse
from .models import *

# Create your views here.
def homepage(request):
        return render(request,'home/homepage.html')

def dynamicDD(request):
        filtereduniversity = University.objects.all()

        coursefilter = request.GET.get('selected_course')
        locationfilter = request.GET.get('selected_location')
        tuitionfilter = request.GET.get('selected_tuition')
        passingratefilter = request.GET.get('selected_passingrate')
        searchquery = request.GET.get('searchquery')

        filtereduniversity = University.objects.all()

        if searchquery != '' and searchquery is not None:
                filtereduniversity = filtereduniversity.filter(name__icontains=searchquery)

        if coursefilter != 'None' and coursefilter is not None:
                filtereduniversity = filtereduniversity.filter(universitycourse__course__name=coursefilter)
                

        if locationfilter != 'None' and locationfilter is not None:
                filtereduniversity = filtereduniversity.filter(location=locationfilter)

        if tuitionfilter != '' and tuitionfilter is not None and coursefilter != 'None' and coursefilter is not None:
                filtereduniversity = filtereduniversity.filter(
                        universitycourse__course__name=coursefilter,
                        universitycourse__estimated_tuition_minimum__lte=tuitionfilter,
                        universitycourse__estimated_tuition_maximum__gt=tuitionfilter
                )

        if passingratefilter != '' and passingratefilter is not None and coursefilter != 'None' and coursefilter is not None:
                filtereduniversity = filtereduniversity.filter(
                        universitycourse__course__name=coursefilter,
                        universitycourse__board_passing_rate__lt=passingratefilter
                )      

        context = {"universities" : filtereduniversity, "coursefilter":coursefilter}
        return render(request,'home/dynamicDD.html',context)

#def filter(request):
        #filtereduniversity = University.objects.all()
        #courses = Course.objects.all()

        #myFilter = FilterCourse(request.GET, queryset=filtereduniversity)
        #filtereduniversity = myFilter.qs

        #context = {'filtereduniversity': filtereduniversity, 'myFilter':myFilter}

        #return render(request,'home/filter.html',context)

