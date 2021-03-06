from django.shortcuts import render, render_to_response
from .models import Me, Education, PlaceOfWork, Hobby

# Create your views here.
def main(request):
    me = Me.objects.filter(id=1)[0]
    context = {'me': me}
    return render(request, "index.html", context)

def education(request):
    me = Me.objects.filter(id=1)[0]
    education_places = Education.objects.all()
    context = {'education_places': education_places, 'me': me}
    return render(request, "education.html", context)

def work_places(request):
    me = Me.objects.filter(id=1)[0]
    work_places = PlaceOfWork.objects.all()
    context = {'work_places': work_places, 'me': me}
    return render(request, "work.html", context)

def work_place(request, id):
    place = PlaceOfWork.objects.get(pk = id)
    context = {'place': place}
    return render(request, "work_place.html", context)

def hobby(request):
    hobbies = Hobby.objects.all()
    context = {'hobbies': hobbies}
    return render(request, "hobby.html", context)
