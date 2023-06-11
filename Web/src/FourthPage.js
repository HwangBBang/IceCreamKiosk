import "./buttons.css";

function FourthPage({ onClick }) {
  return (
    <div className="App">
      <header className="App-header" onClick={onClick}>
        <h1>SecondPage</h1>
        <div>
          <div className="btn-container">
            <a href="#" className="btn-two blue rounded size">
              15 minutes
            </a>
            <a href="#" className="btn-two blue rounded size">
              30 minutes
            </a>
          </div>
          <div className="btn-container">
            <a href="#" className="btn-two blue rounded size">
              an hour
            </a>
            <a href="#" className="btn-two blue rounded size">
              two hours
            </a>
          </div>
        </div>
      </header>
    </div>
  );
}

export default FourthPage;
