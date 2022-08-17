from django.shortcuts import render
from breed_page.breed_app.models import Breed, Coat

# Create your views here.
def index(request):
    breeds = Breed.objects.all()
    context = {'breeds': []}
    for breed in breeds:
        context['breeds'].append({'detailed_link': f"detailed/{breed.id}", 'name': breed.name, 'image_path': breed.image, 'country': breed.country})

    return render(request, 'index.html', context)


def detailed(request, id):
    breed = Breed.objects.get(pk=id)
    predecessors =  breed.predecessor.all()
    context = {
        'breed': breed, 
        'coats': ', '.join([coat.name for coat in breed.coat.all()]), 
        'disciplines': ', '.join([discipline.name for discipline in breed.discipline.all()]), 
        'predecessors': []
    }
    
    for predecessor in predecessors:
        context['predecessors'].append({'link': f"{predecessor.id}", 'name': predecessor.name})
    
    return render(request, 'detailed.html', context)