import React from "react";
import ReactDOM from "react-dom/client";
import { useState } from "react";
import "./index.css";

import App from "./App";
import FirstPage from "./FirstPage";
import SecondPage from "./SecondPage";
import ThirdPage from "./ThirdPage";
import FourthPage from "./FourthPage";
import FifthPage from "./FifthPage";
const root = ReactDOM.createRoot(document.getElementById("root"));

// Eat In 을 클릭했었다면, FifthPage 컴포넌트를 렌더링합니다.
function ThirdToFifth() {
  root.render(
    <React.StrictMode>
      <FifthPage />
    </React.StrictMode>
  );
}

// Take out 을 클릭했었다면, FifthPage 컴포넌트를 렌더링합니다.
function FourthToFifth() {
  root.render(
    <React.StrictMode>
      <FifthPage />
    </React.StrictMode>
  );
}

// Take out 을 클릭했었다면, FourthPage 컴포넌트를 렌더링합니다.
function ThirdToFourth() {
  root.render(
    <React.StrictMode>
      <FourthPage />
    </React.StrictMode>
  );
}

// Size 를 선택하면, ThirdPage 컴포넌트를 렌더링합니다.
function SecondToThird(selectedSize) {
  root.render(
    <React.StrictMode>
      <ThirdPage selectedSize={selectedSize} />
    </React.StrictMode>
  );
}

// Take out 혹은 Eat In 을 클릭하면, SecondPage 컴포넌트를 렌더링합니다.
function FirstToSecond() {
  root.render(
    <React.StrictMode>
      <SecondPage onNextPage={SecondToThird} />
    </React.StrictMode>
  );
}

// App 의 페이지를 클릭하면,FirstPage 컴포넌트를 렌더링합니다.
function AppToFirstPage() {
  root.render(
    <React.StrictMode>
      <FirstPage onClick={FirstToSecond} />
    </React.StrictMode>
  );
}

// 초기에는 App 컴포넌트를 렌더링합니다.
root.render(
  <React.StrictMode>
    <App onClick={AppToFirstPage} />
  </React.StrictMode>
);
