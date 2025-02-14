import google.generativeai as genai
from rest_framework.views import APIView


class GoogleAuth(APIView):
    pass


class ReportsView(APIView):
    genai.configure(api_key="AIzaSyAfO_84PdUyJCxHCNZVivH4hmbCrm3ToMA")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Explain how AI works")
    print(response.text)
