import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Register from './Register';

const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (event) => {
    event.preventDefault();
    if (username===null || username==='') {
      alert('Username cannot be empty');
    }
    if (password===null || password==='') {
      alert('Password cannot be empty');
    }
    const response = await fetch(`http://127.0.0.1:${process.env.REACT_APP_BACKEND_PORT}/auth/authenticate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    if (response.ok) {
      const data = await response.json();
      localStorage.setItem('userId', data);
      navigate("/home");
    } else {
      alert('Login failed');
    }
  }

  const handleRegister = () => {
    navigate("/register");
  }

  return (
    <form>
      <div>
        <label>Username:</label>
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </div>
      <button type="submit" name='login' onClick={handleLogin}>Login</button>
      <br/>
      <p>New here! Register here.</p>
      <button type='submit' name='register' onClick={handleRegister}>Register</button>
    </form>
  );
};

export default Login;
