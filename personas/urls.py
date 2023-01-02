from django.urls import path
from .views import PersonaList, PersonaDetail, PersonaCreate

urlpatterns = [
    path('', PersonaList.as_view(), name="persona_list"),
    path('persona_detail/<int:pk>/', PersonaDetail.as_view(), name="persona_detail"),
    path('persona_create', PersonaCreate.as_view(), name="persona_create"),
]
