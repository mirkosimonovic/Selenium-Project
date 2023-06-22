from . import views
urlpatterns = [
    path('consultas/', views.obtener_informacion, name='consultas'),
]