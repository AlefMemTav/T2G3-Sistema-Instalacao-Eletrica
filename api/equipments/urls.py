from .views import EquipmentTypeList, EquipmentTypeDetail, EquipmentDetailList, EquipmentDetailDetail, AtmosphericDischargeEquipmentList, AtmosphericDischargeEquipmentDetail, FireAlarmEquipmentList, FireAlarmEquipmentDetail, SructeredCablingEquipmentList, SructeredCablingEquipmentDetail
from django.urls import path

urlpatterns = [
    path('equipment-type/', EquipmentTypeList.as_view()),
    path('equipment-type/<pk>/', EquipmentTypeDetail.as_view()),
    path('equipments/', EquipmentDetailList.as_view()),
    path('equipments/<pk>/', EquipmentDetailDetail.as_view()),
    path('atmospheric-discharges/', AtmosphericDischargeEquipmentList.as_view()),
    path('atmospheric-discharges/<pk>/', AtmosphericDischargeEquipmentDetail.as_view()),
    path('fire-alarms/', FireAlarmEquipmentList.as_view()),
    path('fire-alarms/<pk>/', FireAlarmEquipmentDetail.as_view()),
    path('sructered-cabling/', SructeredCablingEquipmentList.as_view()),
    path('sructered-cabling/<pk>/', SructeredCablingEquipmentDetail.as_view()),

]
