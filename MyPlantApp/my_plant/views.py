from django.shortcuts import render, redirect

from MyPlantApp.my_plant.forms import ProfileCreateForm, PlantForm, PlantDeleteForm, ProfileEditForm, ProfileDeleteForm
from MyPlantApp.my_plant.models import Profile, Plant


def home_page(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }
    return render(request, 'home-page.html', context)


def create_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'create-profile.html', context)


def catalogue(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()
    context = {
        'plants': plants,
        'profile': profile
    }
    return render(request, 'catalogue.html', context)


def create_plant(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = PlantForm()
    else:
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'create-plant.html', context)


def plant_details(request, pk):
    profile = Profile.objects.first()
    plant = Plant.objects.filter(pk=pk).get()
    content = {
        'plant': plant,
        'profile': profile
    }
    return render(request, 'plant-details.html', content)


def edit_plant(request, pk):
    profile = Profile.objects.first()
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantForm(instance=plant)
    else:
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'plant': plant,
        'profile': profile
    }
    return render(request, 'edit-plant.html', context)


def delete_plant(request, pk):
    profile = Profile.objects.first()
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'plant': plant,
        'profile': profile
    }
    return render(request, 'delete-plant.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants
    }
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile-details')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('home-page')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'delete-profile.html', context)