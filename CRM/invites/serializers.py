from rest_framework import serializers
from .models import Invitation



class InvitationSerializer(serializers.ModelSerializer):
    class meta:
        model = Invitation
        fields = ['email', 'role']

    

    


