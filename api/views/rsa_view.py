from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.rsa import rsa_encrypt, rsa_decrypt, generate_rsa_keys
# Create your views here.

private_key, public_key = generate_rsa_keys()

@api_view(['GET', 'POST'])
def encrypt_rsa(request):
    data = request.data
    text = data.get('text', '')
    result = rsa_encrypt(text, public_key)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_rsa(request):
    data = request.data
    text = data.get('text', '')
    result = rsa_decrypt(text, private_key)
    return Response({"result": result})