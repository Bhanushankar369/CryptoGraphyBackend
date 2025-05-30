from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.elliptic import ecc_encrypt, ecc_decrypt, derive_shared_key, generate_ecc_keys
# Create your views here.

private1, public1 = generate_ecc_keys()
private2, public2 = generate_ecc_keys()

key1 = derive_shared_key(private1, public2)
key2 = derive_shared_key(private2, public1)

@api_view(['GET', 'POST'])
def encrypt_ecc(request):
    data = request.data
    text = data.get('text', '')
    result = ecc_encrypt(text, key1)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_ecc(request):
    data = request.data
    text = data.get('text', '')
    result = ecc_decrypt(text, key2)
    return Response({"result": result})