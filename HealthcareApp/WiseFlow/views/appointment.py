from rest_framework.views import APIView
from rest_framework.response import Response

from appointments.models import Appointment
from WiseFlow.serializers import AppointmentSerializer

class AppointmentView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            appointment = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)