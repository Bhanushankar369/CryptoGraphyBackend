from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.myszkowskiCipher import myszkowski_encrypt, myszkowski_decrypt
# Create your views here.

@api_view(['GET', 'POST'])
def encrypt_myszkowski(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = myszkowski_encrypt(text, key)
    return Response({"result": result}) 

@api_view(['GET', 'POST'])
def decrypt_myszkowski(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = myszkowski_decrypt(text, key)
    return Response({"result": result})