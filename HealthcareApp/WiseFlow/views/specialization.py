from rest_framework.views import APIView
from rest_framework.response import Response
from appointments.models import Specialization
from WiseFlow.serializers import SpecializationSerializer

class SpecializationView(APIView):
    def get(self, request):
        specializations = Specialization.objects.all()
        serializer = SpecializationSerializer(specializations, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            specialization = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
