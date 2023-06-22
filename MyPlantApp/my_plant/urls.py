from django.urls import path, include
from MyPlantApp.my_plant.views import home_page, create_profile, catalogue, create_plant, plant_details, edit_plant,\
    delete_plant, profile_details, edit_profile, delete_profile

urlpatterns = [
    path('', home_page, name='home-page'),
    path('profile/', include([
        path('create/', create_profile, name='create-profile'),
        path('details/', profile_details, name='profile-details'),
        path('edit/', edit_profile, name='edit-profile'),
        path('delete/', delete_profile, name='delete-profile')
    ])),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', create_plant, name='create-plant'),
    path('details/<int:pk>/', plant_details, name='plant-details'),
    path('edit/<int:pk>/', edit_plant, name='edit-plant'),
    path('delete/<int:pk>/', delete_plant, name='delete-plant')
]