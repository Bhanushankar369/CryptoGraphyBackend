import React from 'react'
import './App.css'
import { useNavigate } from 'react-router-dom';

function Home() {
    const navigate = useNavigate();
  return (
    <div className="home">
        <nav className="navbar">
            <div className="logo heading" onClick={() => navigate('/')}>CG</div>
            <div className="contents">
                <button className="Stength_calc" onClick={() => navigate('/passwordstrength')}>Password Strength Calc</button>
                <button className="about_page">About Page</button>
                <button className="about_creator">About Creator</button>
            </div>
        </nav>
        <div className="container">
            <div className="substitution heading">
                <div className="title">Substitution Techniques</div>
                <div className="buttons">
                    <button className="caesar_cipher" onClick={() => navigate('/ceasar')}>Caesar Cipher</button>
                    <button className="playfair_cipher" onClick={() => navigate('/playfair')}>Playfair Cipher</button>
                    <button className="hill_cipher" onClick={() => navigate('/hill')}>Hill Cipher</button>
                    <button className="onetimepad" onClick={() => navigate('/otp')}>One Time PAD</button>
                </div>
            </div>
            <div className="transposition heading">
                <div className="title">Transposition Techniques</div>
                <div className="buttons">
                    <button className="railfence_cipher" onClick={() => navigate('/railfence')}>Rail Fence Cipher</button>
                    <button className="myszkowski-cipher" onClick={() => navigate('/myszkowski')}>Myszkowski Cipher</button>
                    <button className="route_cipher" onClick={() => navigate('/routecipher')}>Route Cipher</button>
                    <button className="scytale-Cipher" onClick={() => navigate('/scytale')}>Scytale Cipher</button>
                </div>
            </div>
            <div className="SKE heading">
                <div className="title">Symmetric Key Encryption Techniques</div>
                <div className="buttons">
                    <button className="DES" onClick={() => navigate('/des')}>Data Encryption Standard</button>
                    <button className="AES" onClick={() => navigate('/aes')}>Advanced Encryption Standard</button>
                    <button className="rives_cipher" onClick={() => navigate('/rives')}>Rives Cipher 4(RC4)</button>
                </div>
            </div>
            <div className="AKE heading">
                <div className="title">Asymmetric Key Encryption Techniques</div>
                <div className="buttons">
                    <button className="RSA" onClick={() => navigate('/rsa')}>Rivest Shamir Adleman</button>
                    <button className="ECC" onClick={() => navigate('/ellipticcurve')}>Elliptic Curve Cryptography</button>
                    <button className="elgamal" onClick={() => navigate('/elgamal')}>ElGamal</button>
                </div>
            </div>
        </div>
    </div>
  )
}

export default Home;