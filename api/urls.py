from django.urls import path
from .views import caesar_view, playfair_view, hill_view, otp_view
from .views import railfence_view, myszkowski_view, route_view, scytale_view
from .views import des_view, aes_view, rives_view
from .views import rsa_view,elliptic_view, elgamal_view
from .views import password_view

urlpatterns = [
    path('encrypt/Caesar-Cipher/', caesar_view.encrypt_caesar),
    path('decrypt/Caesar-Cipher/', caesar_view.decrypt_caesar),
    path('encrypt/Playfair-Cipher/', playfair_view.encrypt_playfair),
    path('decrypt/Playfair-Cipher/', playfair_view.decrypt_playfair),
    path('encrypt/Hill-Cipher/', hill_view.encrypt_hill),
    path('decrypt/Hill-Cipher/', hill_view.decrypt_hill),
    path('encrypt/OTP-Cipher/', otp_view.encrypt_otp),
    path('decrypt/OTP-Cipher/', otp_view.decrypt_otp),
    path('encrypt/RailFence-Cipher/', railfence_view.encrypt_railfence),
    path('decrypt/RailFence-Cipher/', railfence_view.decrypt_railfence),
    path('encrypt/Myszkowski-Cipher/', myszkowski_view.encrypt_myszkowski),
    path('decrypt/Myszkowski-Cipher/', myszkowski_view.decrypt_myszkowski),
    path('encrypt/Route-Cipher/', route_view.encrypt_route),
    path('decrypt/Route-Cipher/', route_view.decrypt_route),
    path('encrypt/Scytale-Cipher/', scytale_view.encrypt_scytale),
    path('decrypt/Scytale-Cipher/', scytale_view.decrypt_scytale),
    path('encrypt/Data-Encryption-Standard/', des_view.encrypt_des),
    path('decrypt/Data-Encryption-Standard/', des_view.decrypt_des),
    path('encrypt/Advanced-Encryption-Standard/', aes_view.encrypt_aes),
    path('decrypt/Advanced-Encryption-Standard/', aes_view.decrypt_aes),
    path('encrypt/Rives-Cipher/', rives_view.encrypt_rives),
    path('decrypt/Rives-Cipher/', rives_view.decrypt_rives),
    path('encrypt/RSA-Cipher/', rsa_view.encrypt_rsa),
    path('decrypt/RSA-Cipher/', rsa_view.decrypt_rsa),
    path('encrypt/EllipticCurve-Cipher/', elliptic_view.encrypt_ecc),
    path('decrypt/EllipticCurve-Cipher/', elliptic_view.decrypt_ecc),
    path('encrypt/Elgamal-Cipher/', elgamal_view.encrypt_elgamal),
    path('decrypt/Elgamal-Cipher/', elgamal_view.decrypt_elgamal),
    path('passwordstrength/', password_view.password_crack_time)
]