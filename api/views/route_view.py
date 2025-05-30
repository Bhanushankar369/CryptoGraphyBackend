from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.routeCipher import route_encrypt, route_decrypt
# Create your views here.

@api_view(['GET', 'POST'])
def encrypt_route(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = route_encrypt(text, key)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_route(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = route_decrypt(text, key)
    return Response({"result": result})