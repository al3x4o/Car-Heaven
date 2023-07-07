# •	http://localhost:8000/ - index page
# •	http://localhost:8000/profile/create - profile create page
# •	http://localhost:8000/catalogue/ - catalogue page
# •	http://localhost:8000/car/create/ - car create page
# •	http://localhost:8000/car/<car-id>/details/ - car details page
# •	http://localhost:8000/car/<car-id>/edit/ - car edit page
# •	http://localhost:8000/car/<car-id>/delete/ - car delete page
# •	http://localhost:8000/profile/details/ - profile details page
# •	http://localhost:8000/profile/edit/ - profile edit page
# •	http://localhost:8000/profile/delete/ - profile delete page
from django.urls import path, include

from car_collection.web.views import index, details_car, create_car, edit_car, delete_car, details_profile, \
    create_profile, edit_profile, delete_profile, catalogue

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('details/', details_profile, name='details profile'),
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('car/', include([
        path('details/<int:pk>/', details_car, name='details car'),
        path('create/', create_car, name='create car'),
        path('edit/<int:pk>/', edit_car, name='edit car'),
        path('delete/<int:pk>/', delete_car, name='delete car'),
    ])),
)
