from django.urls import path

from .views import PerevalsViewset

urlpatterns = [
    path('', PerevalsViewset.as_view({'get': 'list'}), name='perevals_list'),
    path('<int:pk/', PerevalsViewset.as_view({'get': 'list'}), name='pereval_detail')
]