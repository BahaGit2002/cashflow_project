from django.urls import path
from cashflow.views import (
    IndexView, RecordCreateView, RecordEditView, RecordDeleteView,
    StatusAddAPIView, StatusEditAPIView, StatusDeleteAPIView,
    TypeAddAPIView, TypeEditAPIView, TypeDeleteAPIView,
    CategoryAddAPIView, CategoryEditAPIView, CategoryDeleteAPIView,
    ManageReferencesView, GetCategoriesAPIView
)

app_name = 'cashflow'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('record/create/', RecordCreateView.as_view(), name='record_create'),
    path('record/<int:pk>/edit/', RecordEditView.as_view(), name='record_edit'),
    path('record/<int:pk>/delete/', RecordDeleteView.as_view(), name='record_delete'),
    path('references/', ManageReferencesView.as_view(), name='manage_references'),
    path('references/status/add/', StatusAddAPIView.as_view(), name='status_add'),
    path('references/status/edit/', StatusEditAPIView.as_view(), name='status_edit'),
    path('references/status/delete/', StatusDeleteAPIView.as_view(), name='status_delete'),
    path('references/type/add/', TypeAddAPIView.as_view(), name='type_add'),
    path('references/type/edit/', TypeEditAPIView.as_view(), name='type_edit'),
    path('references/type/delete/', TypeDeleteAPIView.as_view(), name='type_delete'),
    path('references/category/add/', CategoryAddAPIView.as_view(), name='category_add'),
    path('references/category/edit/', CategoryEditAPIView.as_view(), name='category_edit'),
    path('references/category/delete/', CategoryDeleteAPIView.as_view(), name='category_delete'),
    path('api/categories/<int:type_id>/', GetCategoriesAPIView.as_view(), name='get_categories'),
]
