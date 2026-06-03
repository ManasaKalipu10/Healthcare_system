from rest_framework.views import APIView
from rest_framework.response import Response

from WiseFlow.services.impl.ai_service import AIService


class ChatBotView(APIView):

    def post(self, request):

        symptoms = request.data.get("symptoms")

        ai_service = AIService()

        specialization = ai_service.detect_specialization(symptoms)

        return Response({
            "symptoms": symptoms,
            "specialization": specialization
        })