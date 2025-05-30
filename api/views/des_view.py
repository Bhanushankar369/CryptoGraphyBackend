from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.des import des_encrypt, des_decrypt
# Create your views here.

@api_view(['GET', 'POST'])
def encrypt_des(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = des_encrypt(text, key)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_des(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = des_decrypt(text, key)
    return Response({"result": result})