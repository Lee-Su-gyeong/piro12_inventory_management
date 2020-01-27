from django.shortcuts import render, get_object_or_404, redirect

from .forms import PeopleForm
from .models import People

def people_list(request):
    peoples = People.objects.all()
    context = {
        'peoples': peoples
    }
    return render(request, 'people/people_list.html', context)

def people_detail(request, pk):
    people = get_object_or_404(People, pk=pk)
    return render(request, 'people/people_detail.html', {'people': people})

def people_create(request):
    if request.method == "POST":
        form = PeopleForm(request.POST)
        if form.is_valid():
            people = form.save(commit=False)
            people.save()
            return redirect('people_detail', pk=people.pk)
    else:
        form = PeopleForm()
    return render(request, 'people/people_create.html', {'form': form})

def people_update(request, pk):
    people = get_object_or_404(People, pk=pk)
    if request.method == "POST":
        form = PeopleForm(request.POST, instance=people)
        if form.is_valid():
            people = form.save(commit=False)
            people.save()
            return redirect('people_detail', pk=people.pk)
    else:
        form = PeopleForm(instance=people)
    return render(request, 'people/people_create.html', {'form': form})

def people_delete(request, pk):
    people = People.objects.get(id=pk)
    people.delete()
    peoples = People.objects.all()
    context = {
        'peoples': peoples
    }
    return render(request, 'people/people_list.html', context)

