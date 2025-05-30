from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.oneTimePad import otp_encrypt, otp_decrypt

@api_view(['GET', 'POST'])
def encrypt_otp(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = otp_encrypt(text, key)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_otp(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = otp_decrypt(text, key)
    return Response({"result": result})