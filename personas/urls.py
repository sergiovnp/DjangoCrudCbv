from django.urls import path
from .views import PersonaList, PersonaDetail

urlpatterns = [
    path('', PersonaList.as_view(), name="persona_list"),
    path('persona_detail/<int:pk>/', PersonaDetail.as_view(), name="persona_detail"),
]
