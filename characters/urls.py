from django.urls import path
from .views import Homepage, CharactersListView, CharactersDetailView, CharactersCreateView

urlpatterns = (
    path('', Homepage.as_view(), name="home"),
    path('characters', CharactersListView.as_view(), name="characters"),
    path('character/<int:pk>', CharactersDetailView.as_view(), name="character"),
    path('character/new', CharactersCreateView.as_view(), name="character_new"),
)

