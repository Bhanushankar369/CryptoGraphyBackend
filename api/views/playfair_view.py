from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.playfair import playfair_encrypt, playfair_decrypt

@api_view(['GET', 'POST'])
def encrypt_playfair(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = playfair_encrypt(text, key)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_playfair(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = playfair_decrypt(text, key)
    return Response({"result": result})