from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Person, Course,Department
from .forms import PersonCreationForm

#  Create your views here.

def person_create_view(request):

    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Oder Placed Successfully")
            return redirect('person_add')
    return render(request, 'home.html', {'form': form})

def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})

# AJAX
def load_course(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id)
    return render(request, 'city_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

