from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from places.models import Area
from .models import  *
from .serializers import *
from .permissions import *
from rest_framework import status

class PersonalEquipmentCategoryCreate(generics.CreateAPIView):
    queryset = PersonalEquipmentCategory.objects.all()
    serializer_class = PersonalEquipmentCategorySerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def create(self, request, *args, **kwargs):

        if(IsOwner):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(place_owner=request.user.place_owner)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PersonalEquipmentCategoryList(generics.ListAPIView):
    queryset = PersonalEquipmentCategory.objects.all()
    serializer_class = PersonalEquipmentCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        system_id = self.kwargs['system_id']
        return PersonalEquipmentCategory.objects.filter(system_id=system_id)

class PersonalEquipmentCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalEquipmentCategory.objects.all()
    serializer_class = PersonalEquipmentCategorySerializer
    permission_classes = [IsAuthenticated]

class GenericEquipmentCategoryList(generics.ListAPIView):
    queryset = GenericEquipmentCategory.objects.all()
    serializer_class = GenericEquipmentCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        system_id = self.kwargs['system_id']
        return GenericEquipmentCategory.objects.filter(system_id=system_id)

class GenericEquipmentCategoryDetail(generics.RetrieveAPIView):
    queryset = GenericEquipmentCategory.objects.all()
    serializer_class = GenericEquipmentCategorySerializer
    permission_classes = [IsAuthenticated]

class EquipmentList(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(place_owner__user=user)

class EquipmentCreate(generics.CreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'request': self.request
        })
        return context

class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsOwner, IsAuthenticated]

class EquipmentPhotoList(generics.ListCreateAPIView):
    queryset = EquipmentPhoto.objects.all()
    serializer_class = EquipmentPhotoSerializer
    permission_classes = [IsEquipmentOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(equipment__place_owner__user=user)

class EquipmentPhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipmentPhoto.objects.all()
    serializer_class = EquipmentPhotoSerializer
    permission_classes = [IsEquipmentOwner, IsAuthenticated]

class RefrigerationEquipmentList(generics.ListCreateAPIView):
    queryset = RefrigerationEquipment.objects.all()
    serializer_class = RefrigerationEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return RefrigerationEquipment.objects.filter(area__place__place_owner=user.place_owner)

    def create(self, request, *args, **kwargs):
        data = request.data.copy() 
        data["system"] = 9
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
    
class RefrigerationEquipmentByAreaList(generics.ListAPIView):
    serializer_class = RefrigerationEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        area_id = self.kwargs['area_id']
        return RefrigerationEquipment.objects.filter(area_id=area_id)

class RefrigerationEquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RefrigerationEquipment.objects.all()
    serializer_class = RefrigerationEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

class FireAlarmEquipmentList(generics.ListCreateAPIView):
    queryset = FireAlarmEquipment.objects.all()
    serializer_class = FireAlarmEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FireAlarmEquipment.objects.filter(area__place__place_owner=user.place_owner)

    def create(self, request, *args, **kwargs):
        data = request.data.copy() 
        data["system"] = 8
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

class FireAlarmEquipmentByAreaList(generics.ListAPIView):
    serializer_class = FireAlarmEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        area_id = self.kwargs['area_id']
        return FireAlarmEquipment.objects.filter(area_id=area_id)

class FireAlarmEquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FireAlarmEquipment.objects.all()
    serializer_class = FireAlarmEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

class AtmosphericDischargeEquipmentList(generics.ListCreateAPIView):
    queryset = AtmosphericDischargeEquipment.objects.all()
    serializer_class = AtmosphericDischargeEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return AtmosphericDischargeEquipment.objects.filter(area__place__place_owner=user.place_owner)

    def create(self, request, *args, **kwargs):
        data = request.data.copy() 
        data["system"] = 7
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

class AtmosphericDischargeEquipmentByAreaList(generics.ListAPIView):
    serializer_class = AtmosphericDischargeEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        area_id = self.kwargs['area_id']
        return AtmosphericDischargeEquipment.objects.filter(area_id=area_id)

class AtmosphericDischargeEquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AtmosphericDischargeEquipment.objects.all()
    serializer_class = AtmosphericDischargeEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

class StructuredCablingEquipmentList(generics.ListCreateAPIView):
    queryset = StructuredCablingEquipment.objects.all()
    serializer_class = StructuredCablingEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return StructuredCablingEquipment.objects.filter(area__place__place_owner=user.place_owner)

    def create(self, request, *args, **kwargs):
        data = request.data.copy() 
        data["system"] = 6
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

class StructuredCablingEquipmentByAreaList(generics.ListAPIView):
    serializer_class = StructuredCablingEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        area_id = self.kwargs['area_id']
        return StructuredCablingEquipment.objects.filter(area_id=area_id)

class StructuredCablingEquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StructuredCablingEquipment.objects.all()
    serializer_class = StructuredCablingEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

class DistributionBoardEquipmentList(generics.ListCreateAPIView):
    queryset = DistributionBoardEquipment.objects.all()
    serializer_class = DistributionBoardEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return DistributionBoardEquipment.objects.filter(area__place__place_owner=user.place_owner)
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy() 
        data["system"] = 5
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

class DistributionBoardEquipmentByAreaList(generics.ListAPIView):
    serializer_class = DistributionBoardEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        area_id = self.kwargs['area_id']
        return DistributionBoardEquipment.objects.filter(area_id=area_id)

class DistributionBoardEquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DistributionBoardEquipment.objects.all()
    serializer_class = DistributionBoardEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

class ElectricalCircuitEquipmentList(generics.ListCreateAPIView):
    queryset = ElectricalCircuitEquipment.objects.all()
    serializer_class = ElectricalCircuitEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ElectricalCircuitEquipment.objects.filter(area__place__place_owner=user.place_owner)
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy() 
        data["system"] = 4
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

class ElectricalCircuitEquipmentByAreaList(generics.ListAPIView):
    serializer_class = ElectricalCircuitEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        area_id = self.kwargs['area_id']
        return ElectricalCircuitEquipment.objects.filter(area_id=area_id)

class ElectricalCircuitEquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElectricalCircuitEquipment.objects.all()
    serializer_class = ElectricalCircuitEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

class ElectricalLineEquipmentList(generics.ListCreateAPIView):
    queryset = ElectricalLineEquipment.objects.all()
    serializer_class = ElectricalLineEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ElectricalLineEquipment.objects.filter(area__place__place_owner=user.place_owner)
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy() 
        data["system"] = 3
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
    
class ElectricalLineEquipmentByAreaList(generics.ListAPIView):
    serializer_class = ElectricalLineEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        area_id = self.kwargs['area_id']
        return ElectricalLineEquipment.objects.filter(area_id=area_id)
    
class ElectricalLineEquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElectricalLineEquipment.objects.all()
    serializer_class = ElectricalLineEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

class ElectricalLoadEquipmentList(generics.ListCreateAPIView):
    queryset = ElectricalLoadEquipment.objects.all()
    serializer_class = ElectricalLoadEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ElectricalLoadEquipment.objects.filter(area__place__place_owner=user.place_owner)
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy() 
        data["system"] = 2
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

class ElectricalLoadEquipmentByAreaList(generics.ListAPIView):
    serializer_class = ElectricalLoadEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        area_id = self.kwargs['area_id']
        return ElectricalLoadEquipment.objects.filter(area_id=area_id)

class ElectricalLoadEquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElectricalLoadEquipment.objects.all()
    serializer_class = ElectricalLoadEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

class IluminationEquipmentList(generics.ListCreateAPIView):
    queryset = IluminationEquipment.objects.all()
    serializer_class = IluminationEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return IluminationEquipment.objects.filter(area__place__place_owner=user.place_owner)

    def create(self, request, *args, **kwargs):
        data = request.data.copy() 
        data["system"] = 1
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

class IluminationEquipmentByAreaList(generics.ListAPIView):
    serializer_class = IluminationEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]

    def get_queryset(self):
        area_id = self.kwargs['area_id']
        return IluminationEquipment.objects.filter(area_id=area_id)

class IluminationEquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IluminationEquipment.objects.all()
    serializer_class = IluminationEquipmentSerializer
    permission_classes = [IsAreaOwner, IsAuthenticated]