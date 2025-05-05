from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .serializers import InvitationSerializer
from .models import Invitation
from rest_framework.response import Response

# Create your views here.


class InvitationView(APIView):
    permission_classes= [IsAdminUser]
    
    def post(self, request):
        email = request.data.get('email')
        role = request.data.get('role')
        
        invitation = Invitation.objects.create(email = email, role = role , company = request.user.company)
        invitation.send_invitation()
        return Response({
            'message': "Invitation sent successfully"
        })
        
        




