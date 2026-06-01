from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from WiseFlow.services.impl.patient_service_impl import PatientServiceImpl
from WiseFlow.serializers import PatientSerializer

class PatientViewSet(viewsets.ViewSet): 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.patient_service = PatientServiceImpl()

    @action(detail=False, methods=['get'])
    def get_all_patients(self, request):
        patients = self.patient_service.get_all_patients()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)    
    
    @action(detail = False, methods=['get'])
    def get_patient_details(self, request):
        patient_id = request.query_params.get("patient_id")
        patient = self.patient_service.get_patient_details(patient_id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def create_patient(self, request):
        patient = self.patient_service.create_patient(request.data)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    @action(detail=False, methods=['put'])
    def update_patient_details(self, request):
        patient_id = request.data.get("patient_id")
        patient = self.patient_service.update_patient(patient_id, request.data)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def delete_patient(self, request):
        patient_id = request.data.get("patient_id")
        self.patient_service.delete_patient(patient_id)
        return Response({"message": "Patient deleted successfully"})