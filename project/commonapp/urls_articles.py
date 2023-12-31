
from django.urls import path
# Импортируем созданные нами представления
from .views import ArticlesList, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete, ArticleSearch
urlpatterns = [
   path('', ArticlesList.as_view(), name='article_list'),
   path('<int:pk>', ArticleDetail.as_view(), name='article_detail'),
   path('create/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('search/', ArticleSearch.as_view(), name='new_search'),
]