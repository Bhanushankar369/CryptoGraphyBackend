from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.aes import aes_encrypt, aes_decrypt
# Create your views here.

@api_view(['GET', 'POST'])
def encrypt_aes(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = aes_encrypt(text, key)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_aes(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = aes_decrypt(text, key)
    return Response({"result": result})