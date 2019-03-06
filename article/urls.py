from django.urls import path

from article.views import article_detail, acticle_list

urlpatterns = [
    path('<int:article_id>',article_detail,name="article_detail"),
    path('',acticle_list,name="article_list")

]


