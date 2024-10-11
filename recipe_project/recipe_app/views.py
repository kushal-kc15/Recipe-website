from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'list.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['ingredients_list'] = recipe.ingredients.split(',')  # Split ingredients into a list
        context['process_list'] = recipe.process.split('.')
        return context

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['name', 'category', 'description', 'process', 'ingredients', 'picture']
    template_name = 'form.html'
    success_url = reverse_lazy('recipe_list')

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['name', 'category', 'description', 'process', 'ingredients', 'picture']
    template_name = 'form.html'
    success_url = reverse_lazy('recipe_list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('recipe_list')
