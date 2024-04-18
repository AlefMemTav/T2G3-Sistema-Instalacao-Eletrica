from .views import EquipmentTypeList, EquipmentTypeDetail, EquipmentList, EquipmentDetail
from django.urls import path

urlpatterns = [

    path('equipment-type/', EquipmentTypeList.as_view()),
    path('equipment-type/<pk>/', EquipmentTypeDetail.as_view()),
    path('equipments/', EquipmentList.as_view()),
    path('equipments/<pk>/', EquipmentDetail.as_view())

]