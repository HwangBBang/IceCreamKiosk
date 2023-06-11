import "./App.css";
import "./buttons.css";
import React, { useState } from "react";

function FirstPage({ onClick }) {
  const [takeout, setTakeout] = useState(false);
  const [eatIn, setEatIn] = useState(false);

  const handleTakeoutClick = () => {
    setTakeout(true);
    setEatIn(false);
    console.log("clicked takeout");
  };

  const handleEatInClick = () => {
    setTakeout(false);
    setEatIn(true);
    console.log("clicked Eat In");
  };
  return (
    <div className="App">
      <header className="App-header">
        <h1>How to Do ?</h1>
        <div className="btn-container">
          <a
            href="#"
            className="btn-two blue rounded"
            onClick={(handleEatInClick, onClick)}
          >
            Eat In
          </a>
          <a
            href="#"
            className="btn-two blue rounded"
            onClick={(handleEatInClick, onClick)}
          >
            Take Out
          </a>
        </div>
      </header>
    </div>
  );
}

export default FirstPage;
