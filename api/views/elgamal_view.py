from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.elgamal import elgamal_encrypt, elgamal_decrypt, generate_keys
# Create your views here.

# global public_key
# global private_key

public_key, private_key = generate_keys()

@api_view(['GET', 'POST'])
def encrypt_elgamal(request):
    data = request.data
    text = data.get('text', '')
    # text = "Bhanu shankar"
    result = elgamal_encrypt(text, public_key)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_elgamal(request):
    data = request.data
    text = data.get('text', '')
    result = elgamal_decrypt(text, private_key, public_key[0])
    return Response({"result": result})