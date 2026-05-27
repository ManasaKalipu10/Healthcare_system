from rest_framework.views import APIView
from rest_framework.response import Response

from appointments.models import Patient
from WiseFlow.serializers import PatientSerializer  

class PatientView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            patient = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)