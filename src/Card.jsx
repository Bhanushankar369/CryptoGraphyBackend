import React, {useState} from 'react'
import './Card.css'

const Card = (props) => {

    const [text, setText] = useState('');
    const [key, setKey] = useState('');
    const [output, setOutput] = useState('');

    const handleEncrypt = async () => {
        const response = await fetch(`http://127.0.0.1:8000/encrypt/${props.title}/`,{
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({text, key}),
        });
        const data = await response.json();
        setOutput(data.result);
    }

    const handleDecrypt = async () =>{
        const response = await fetch(`http://127.0.0.1:8000/decrypt/${props.title}/`,{
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, key }),
        });
        const data = await response.json();
        setOutput(data.result);
    }

  return (
    <div className="input-container">
        <nav className="navbar">
            <div className="logo heading">CG</div>
            <div className="contents">
                <button className="Stength_calc">Password Strength Calc</button>
                <button className="about_page">About Page</button>
                <button className="about_creator">About Creator</button>
            </div>
        </nav>
        <div className="input-boxes">
            <div className="title">{props.title}</div>
            <div className="inputs">
                <div className="input">
                    <input 
                        type="text" 
                        className='text'
                        placeholder='Enter Text'
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                    />
                    <input 
                        type={props.keytype} 
                        className='key'
                        placeholder={props.placeholder}
                        value={key}
                        onChange={(e) => setKey(e.target.value)}
                    />
                </div>
                <div className="output">
                    <textarea 
                        readOnly 
                        name="output" 
                        id="output"
                        value={output}
                        placeholder='Output'
                    ></textarea>
                </div>
            </div>
            <div className="EDbuttons">
                <button className="encrypt" onClick={handleEncrypt}>Encrypt</button>
                <button className="decrypt" onClick={handleDecrypt}>Decrypt</button>
            </div>
        </div>
    </div>
  )
}

export default Card