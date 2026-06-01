from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from WiseFlow.services.impl.specializations_service_impl import SpecializationsServiceImpl
from WiseFlow.serializers import SpecializationSerializer

class SpecializationViewSet(viewsets.ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.specialization_service = SpecializationsServiceImpl()

    @action(detail=False, methods=['get'])
    def get_all_specializations(self, request):
        specializations = self.specialization_service.get_all_specializations()
        serializer = SpecializationSerializer(specializations, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def create_specialization(self, request):
        specialization = self.specialization_service.create_specialization(request.data)
        serializer = SpecializationSerializer(specialization)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def get_specialization_details(self, request):
        specialization_id = request.query_params.get("specialization_id")
        specialization = self.specialization_service.get_specialization_details(specialization_id)
        serializer = SpecializationSerializer(specialization)
        return Response(serializer.data)
    
    @action(detail=False, methods=['put'])
    def update_specialization_details(self, request):
        specialization_id = request.data.get("specialization_id")
        specialization = self.specialization_service.update_specialization(specialization_id, request.data)
        serializer = SpecializationSerializer(specialization)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def delete_specialization(self, request):
        specialization_id = request.data.get("specialization_id")
        self.specialization_service.delete_specialization(specialization_id)
        return Response({"message": "Specialization deleted successfully"})