from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.hillCipher import hill_encrypt, hill_decrypt

@api_view(['GET', 'POST'])
def encrypt_hill(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = hill_encrypt(text, key)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_hill(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = hill_decrypt(text, key)
    return Response({"result": result})