import React, { useState, useEffect } from "react";
import "./buttons.css";

function SecondPage({ onNextPage }) {
  const [selectedSize, setSelectedSize] = useState(0);

  const handleClick = (size) => {
    setSelectedSize(size);
  };

  const handleNextPage = () => {
    if (selectedSize > 0) {
      onNextPage(selectedSize);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Choice Size</h1>
        <div>
          <div className="btn-container">
            <a
              href="#"
              className="btn-two blue rounded size"
              onClick={() => handleClick(1)}
            >
              Single
              <span className="price">$2.99</span>
            </a>
            <a
              href="#"
              className="btn-two blue rounded size"
              onClick={() => handleClick(2)}
            >
              Double <span className="price">$4.99</span>
            </a>
            <a
              href="#"
              className="btn-two blue rounded size"
              onClick={() => handleClick(3)}
            >
              Pint <span className="price">$7.99</span>
            </a>
          </div>
          <div className="btn-container">
            <a
              href="#"
              className="btn-two blue rounded size"
              onClick={() => handleClick(4)}
            >
              Quart <span className="price">$13.99</span>
            </a>
            <a
              href="#"
              className="btn-two blue rounded size"
              onClick={() => handleClick(5)}
            >
              Family <span className="price">$18.99</span>
            </a>
            <a
              href="#"
              className="btn-two blue rounded size"
              onClick={() => handleClick(6)}
            >
              HalfGallon <span className="price">$23.99</span>
            </a>
          </div>
        </div>
      </header>
      {selectedSize > 0 && handleNextPage()}
    </div>
  );
}

export default SecondPage;
