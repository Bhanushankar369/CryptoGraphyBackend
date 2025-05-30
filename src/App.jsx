import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './Home';
import Ceasar from './components/substitution Techniques/caesarCipher';
import Playfair from './components/substitution Techniques/playFair';
import Hill from './components/substitution Techniques/hillCipher';
import OTP from './components/substitution Techniques/oneTimePad';
import Railfence from './components/Transposition Techniques/railFence';
import MyszkowskiCipher from './components/Transposition Techniques/myszkowskiCipher';
import RouteCipher from './components/Transposition Techniques/routeCipher';
import Scytale from './components/Transposition Techniques/scytaleCipher';
import DES from './components/Symmetric Key Encryption/DataEncryptionStandard';
import AES from './components/Symmetric Key Encryption/AdvancedEncryptionStandard';
import Rives from './components/Symmetric Key Encryption/RivesCipher';
import RSA from './components/Asymmetric Key Encryption/RivestShamirAdleman';
import EllipticCurve from './components/Asymmetric Key Encryption/EllipticCurve';
import Elgamal from './components/Asymmetric Key Encryption/ElGamal';
import PasswordCrack from './components/passwordCrack';

function App(){
    return(
        <Router>
            <Routes>
                <Route path="/" element={<Home />}></Route>
                <Route path="/ceasar" element={<Ceasar />}></Route>
                <Route path="/playfair" element={<Playfair />}></Route>
                <Route path="/hill" element={<Hill />}></Route>
                <Route path="/otp" element={<OTP />}></Route>
                <Route path="/railfence" element={<Railfence />}></Route>
                <Route path="/myszkowski" element={<MyszkowskiCipher />}></Route>
                <Route path="/routecipher" element={<RouteCipher/>}></Route>
                <Route path="/scytale" element={<Scytale />}></Route>
                <Route path="/des" element={<DES />}></Route>
                <Route path="/aes" element={<AES/>}></Route>
                <Route path="/rives" element={<Rives />}></Route>
                <Route path="/rsa" element={<RSA />}></Route>
                <Route path="/ellipticcurve" element={<EllipticCurve/>}></Route>
                <Route path="/elgamal" element={<Elgamal />}></Route>
                <Route path="/passwordstrength" element={<PasswordCrack/>}></Route>
            </Routes>
        </Router>
    );
}
export default App;