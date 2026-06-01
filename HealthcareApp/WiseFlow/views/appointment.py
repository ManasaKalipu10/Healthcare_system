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

        existing = Appointment.objects.filter(
            doctor=request.data["doctor"],
            appointment_date=request.data["appointment_date"],
            appointment_time=request.data["appointment_time"]
        ).exists()

        if existing:
            return Response(
                {"error": "Doctor already has an appointment at this time slot"},
                status=400
            )

        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)