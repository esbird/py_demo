from django.urls import path

from .views import blog_list,blog_detail,blog_with_type,blog_with_date

urlpatterns = [
    path('<int:blog_id>',blog_detail,name="blog_detail"),
    path('',blog_list,name="blog_list"),
    path('type/<int:blog_type_pk>',blog_with_type,name="blog_with_type"),
    path('date/<int:year>/<int:month>',blog_with_date,name="blog_with_date"),

]


