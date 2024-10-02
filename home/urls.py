from django.urls import path
from .views import homepage, select_by_category, announcement_detail
urlpatterns = [
    path('', homepage, name='homepage'),
    path('category/<int:category_id>', select_by_category, name='category'),
    path('announcement/<int:announcement_id>', announcement_detail, name='detail'),
]