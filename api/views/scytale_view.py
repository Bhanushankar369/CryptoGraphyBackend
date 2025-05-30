from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.scytaleCipher import scytale_encrypt, scytale_decrypt
# Create your views here.

@api_view(['GET', 'POST'])
def encrypt_scytale(request):
    data = request.data
    text = data.get('text', '')
    key = int(data.get('key', 0))
    result = scytale_encrypt(text, key)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_scytale(request):
    data = request.data
    text = data.get('text', '')
    key = int(data.get('key', 0))
    result = scytale_decrypt(text, key)
    return Response({"result": result})