from django.shortcuts import render,redirect
from .models import Pet
from .forms import PetForm

def list_view(request):
    context = {
        "pets": Pet.objects.all(),
    }
    return render(request, 'pets_list.html', context)

def detail_view(request,pet_id):
    context = {
        "pet": Pet.objects.get(id=pet_id),
    }

    return render(request, 'pets_detail.html', context)


def create_pet(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pets_list")
    context = {
        "form":form
    }
    return render(request, 'create_pet.html', context)


def update_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    form = PetForm(instance = pet)
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES, instance = pet)
        if form.is_valid():
            form.save()
            return redirect("pets_detail")
    context = {
        "pet":pet,
        "form":form
    }
    return render(request, 'update_pet.html', context)

def delete_pet(request, pet_id):
    Pet.objects.get(id=pet_id).delete()
    return redirect("pets_list")
