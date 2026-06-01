from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from WiseFlow.services.impl.doctor_service_impl import DoctorServiceImpl
from WiseFlow.serializers import DoctorSerializer

class DoctorViewSet(viewsets.ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.doctor_service = DoctorServiceImpl()

    @action(detail=False, methods=['get'])
    def get_all_doctors(self, request):
        doctors = self.doctor_service.get_all_doctors()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)    
    
    @action(detail = False, methods=['get'])
    def get_doctor_details(self, request):
        doctor_id = request.query_params.get("doctor_id")
        doctor = self.doctor_service.get_doctor_details(doctor_id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def create_doctor(self, request):
        doctor = self.doctor_service.create_doctor(request.data)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    
    @action(detail=False, methods=['put'])
    def update_doctor_details(self, request):
        doctor_id = request.data.get("doctor_id")
        doctor = self.doctor_service.update_doctor(doctor_id, request.data)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def delete_doctor(self, request):
        doctor_id = request.data.get("doctor_id")
        self.doctor_service.delete_doctor(doctor_id)
        return Response({"message": "Doctor deleted successfully"})