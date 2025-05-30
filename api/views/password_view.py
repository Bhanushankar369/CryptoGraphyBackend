from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.password import password_crack_time

@api_view(['GET', 'POST'])
def encrypt_playfair(request):
    data = request.data
    password = data.get('text', '')
    result = password_crack_time(password)
    return Response({"result": result}) 
