from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='create_recipe'),
    path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='update_recipe'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='delete_recipe'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)