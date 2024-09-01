import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';


const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();

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
          navigate(`http://127.0.0.1:${process.env.REACT_APP_BACKEND_PORT}/outfit/view`);
        } else {
          alert('Login failed');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
          <div>
            <label>Email:</label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
          </div>
          <div>
            <label>Phone Number:</label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)}/>
          </div>
          <div>
            <label>Username:</label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
          </div>
          <div>
            <label>Password:</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </div>
          <button type="submit">Register</button>
        </form>
    );
}

export default Register;
