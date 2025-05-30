import React from 'react'
import './password.css'

const passwordCrack = () => {
  return (
    <div className="password-box">
        <nav className="navbar">
            <div className="logo heading">CG</div>
            <div className="contents">
                <button className="Stength_calc">Password Strength Calc</button>
                <button className="about_page">About Page</button>
                <button className="about_creator">About Creator</button>
            </div>
        </nav>
        <div className="values">
            <input type="text" className="password"/>
            <div className="time">0</div>
            <button className='calc'>Calculate</button>
        </div>
    </div>
  )
}

export default passwordCrack