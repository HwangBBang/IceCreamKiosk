// import React, { useState } from "react";
import "./App.css";

/////////////////////
function App({ onClick }) {
  return (
    <div className="App" onClick={onClick}>
      <header className="App-header">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/d/d8/Baskin-Robbins_logo.svg"
          className="App-logo"
          alt="logo"
        />
        <h1>Welcome!</h1>
        <h2>Click anywhere to next ! </h2>
      </header>
    </div>
  );
}

export default App; // App 컴포넌트를 내보내기
