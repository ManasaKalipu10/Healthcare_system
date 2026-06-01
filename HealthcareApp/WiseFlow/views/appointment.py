from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from WiseFlow.services.impl.appointments_service_impl import AppointmentServiceImpl
from WiseFlow.serializers import AppointmentSerializer  

class AppointmentViewSet(viewsets.ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.appointment_service = AppointmentServiceImpl()

    @action(detail=False, methods=['get'])
    def get_all_appointments(self, request):
        appointments = self.appointment_service.get_all_appointments()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)    
    
    @action(detail = False, methods=['get'])
    def get_appointment_details(self, request):
        appointment_id = request.query_params.get("appointment_id")
        appointment = self.appointment_service.get_appointment_details(appointment_id)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def create_appointment(self, request):
        appointment = self.appointment_service.create_appointment(request.data)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    
    @action(detail=False, methods=['put'])
    def update_appointment_details(self, request):
        appointment_id = request.data.get("appointment_id")
        appointment = self.appointment_service.update_appointment(appointment_id, request.data)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def delete_appointment(self, request):
        appointment_id = request.data.get("appointment_id")
        self.appointment_service.delete_appointment(appointment_id)
        return Response({"message": "Appointment deleted successfully"})
    
    @action(detail=False, methods=['get'])
    def check_doctor_slot(self, request):
        doctor_id = request.query_params.get("doctor_id")
        appointment_date = request.query_params.get("appointment_date")
        appointment_time = request.query_params.get("appointment_time")
        doctor_exists = self.appointment_service.check_doctor_slot(doctor_id, appointment_date, appointment_time)
        return Response({"doctor_exists": doctor_exists})