// frontend/src/App.jsx

import React, { useState } from 'react';
import Cadastro from './componenets/Cadastro';
import Login from './componenets/Login';

function App() {
  const [isLogged, setIsLogged] = useState(false);

  return (
    <div className="App">
      {isLogged ? <h1>Você está logado!</h1> : null}
      <Login setIsLogged={setIsLogged} />
      <Cadastro />
    </div>
  );
}

export default App;
