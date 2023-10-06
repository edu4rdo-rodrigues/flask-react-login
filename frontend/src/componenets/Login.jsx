// frontend/src/components/Login.jsx

import React, { useState } from 'react';

function Login({ setIsLogged }) {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      email,
      senha,
    };

    try {
      const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (response.status === 200) {
        // O login foi bem-sucedido, você pode lidar com a resposta aqui.
        console.log('Login bem-sucedido!');
        setIsLogged(true); // Define o estado como logado
      } else {
        // Lidar com erros de autenticação ou outros problemas.
        console.error('Erro ao fazer login.');
      }
    } catch (error) {
      console.error('Erro na solicitação:', error);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="email">E-mail:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="senha">Senha:</label>
          <input
            type="password"
            id="senha"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
