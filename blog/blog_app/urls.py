from .views import main_feed, get_post, filtered_by_category
from django.urls import path


urlpatterns = [
    path('', main_feed),
    path('category/<int:category_code>/', filtered_by_category),
    path('post/<int:post_id>/', get_post)
    ]