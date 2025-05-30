from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.rives import rc4
import base64

@api_view(['POST'])
def encrypt_rives(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = rc4(key, text)
    cipher_b64 = base64.b64encode(result).decode()
    return Response({"result": cipher_b64})

@api_view(['POST'])
def decrypt_rives(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    cipher_bytes = base64.b64decode(text)
    decrypted_bytes = rc4(key, cipher_bytes)
    try:
        plaintext = decrypted_bytes.decode('utf-8')
    except UnicodeDecodeError:
        plaintext = decrypted_bytes.decode('latin-1')
    return Response({"result": plaintext})