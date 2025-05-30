from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ciphers.railFence import rail_fence_encrypt, rail_fence_decrypt

@api_view(['GET', 'POST'])
def encrypt_railfence(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = rail_fence_encrypt(text, key)
    return Response({"result": result}) 
    
@api_view(['GET', 'POST'])
def decrypt_railfence(request):
    data = request.data
    text = data.get('text', '')
    key = data.get('key', '')
    result = rail_fence_decrypt(text, key)
    return Response({"result": result})