from django.urls import path
from . import views


urlpatterns = [
    path('creation/', views.create_post, name='creation'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('profile/<int:id>', views.post_profile, name='profile'),
    path('wishlist/add_to_wishlist/<int:id>', views.add_to_wishlist, name='add-wishlist'),
    path('wishlist/delete_from_wishlist/<int:id>', views.delete_from_wishlist, name='delete-wishlist')
]
