from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from WiseFlow.serializers import DoctorSerializer
from WiseFlow.services.impl.doctor_service_impl import DoctorServiceImpl

class DoctorView(APIView):
    def __init__(self):
        self.doctor_service = DoctorServiceImpl()

    def get(self, request):
        doctors = self.doctor_service.get_all_doctors()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            doctor_data = serializer.validated_data
            doctor = self.doctor_service.create_doctor(doctor_data)
            return Response(DoctorSerializer(doctor).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)