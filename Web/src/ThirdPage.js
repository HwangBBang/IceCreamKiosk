import { useState } from "react";
import "./index.css";
import "./menu.css";

const Choose = ({ selectedSize }) => {
  switch (selectedSize) {
    case "1":
      return "Single";
    case 2:
      return "Double";
    case 3:
      return "Pint";
    case 4:
      return "Quart";
    case 5:
      return "Family";
    case 6:
      return "HalfGallon";
  }
};
// 세 번째 페이지 컴포넌트
const Menu = ({ selectedSize }) => {
  // 예시 데이터: 32개의 이미지 URL
  const flavors = [
    "https://www.baskinrobbins.co.kr/upload/product/1499161015.png",
    "https://www.baskinrobbins.co.kr/upload/product/1528197022.png",
    "https://www.baskinrobbins.co.kr/upload/product/1623256634.png",
    "https://www.baskinrobbins.co.kr/upload/product/1452062933.png",
    "https://www.baskinrobbins.co.kr/upload/product/1670827206.png",
    "https://www.baskinrobbins.co.kr/upload/product/1530775807.png",
    "https://www.baskinrobbins.co.kr/upload/product/1530776851.png",
    "https://www.baskinrobbins.co.kr/upload/product/1530775918.png",
    "https://www.baskinrobbins.co.kr/upload/product/1530775359.png",
    "https://www.baskinrobbins.co.kr/upload/product/1554261647.png",
    "https://www.baskinrobbins.co.kr/upload/product/1530777439.png",
    "https://www.baskinrobbins.co.kr/upload/product/1530778136.png",
    "https://www.baskinrobbins.co.kr/upload/product/1530775514.png",
    "https://www.baskinrobbins.co.kr/upload/product/1530778494.png",
    "https://www.baskinrobbins.co.kr/upload/product/1670827275.png",
    "https://www.baskinrobbins.co.kr/upload/product/1530771632.png",
    "https://www.baskinrobbins.co.kr/upload/product/1691210392.png",
    "https://www.baskinrobbins.co.kr/upload/product/1733291808.png",
    "https://www.baskinrobbins.co.kr/upload/product/1699080694.png",
    "https://www.baskinrobbins.co.kr/upload/product/1743659352.png",
    "https://www.baskinrobbins.co.kr/upload/product/1727918465.png",
    "https://www.baskinrobbins.co.kr/upload/product/1727917740.png",
    "https://www.baskinrobbins.co.kr/upload/product/1696232010.png",
    "https://www.baskinrobbins.co.kr/upload/product/1720745560.png",
    "https://www.baskinrobbins.co.kr/upload/product/1738629805.png",
    "https://www.baskinrobbins.co.kr/upload/product/1530779443.png",
    "https://www.baskinrobbins.co.kr/upload/product/1670825573.png",
    "https://www.baskinrobbins.co.kr/upload/product/1670825733.png",
    "https://www.baskinrobbins.co.kr/upload/product/1670827140.png",
    "https://www.baskinrobbins.co.kr/upload/product/1670825939.png",
    "https://www.baskinrobbins.co.kr/upload/product/1452062882.png",
    "https://www.baskinrobbins.co.kr/upload/product/1696232148.png",
  ];
  const flavorName = [
    "루나 치즈케이크",
    "엄마는 외계인",
    "오레오 쿠키 앤 크림치즈",
    "아몬드 봉봉",
    "민트 초콜릿 칩",
    "슈팅스타",
    "초코나무 숲",
    "뉴욕 치즈케이크",
    "피스타치오 아몬드",
    "베리베리 스트로베리",
    "바람과 함께 사라지다",
    "레인보우 샤베트",
    "자모카 아몬드 훠지",
    "초콜릿 무스",
    "이상한 나라의 솜사탕",
    "초콜릿",
    "사과나라 헬로키티",
    "구름 속 시나몬 롤",
    "아이스 카멜 커피",
    "복숭아로 피치 올려",
    "블랙 슈가 밤",
    "애플 민트",
    "러브미",
    "벅스 버니버니 당근당근",
    "블랙 소르베",
    "사랑에 빠진 딸기",
    "핑크스푼 비긴즈",
    "초코넛 마카다미아",
    "오레오 쿠키 앤 크림",
    "월넛",
    "체리쥬빌레",
    "초코 체리쥬빌레",
  ];

  const AddList = [];
  let i = 0;

  const handleClick = (index) => {
    console.log(`버튼 ${index}이(가) 클릭되었습니다.`);
    // 버튼 클릭 시 수행할 동작 추가
    // 빈 배열에 index 추가
    AddList.push(index);
    AddList[i] = flavorName[AddList[i]];
    console.log("AddList: ", AddList);

    i += 1;
    if (AddList.length === selectedSize) {
      console.log("맛 선택 완료");
    }
  };

  return (
    <div className="menu">
      <h2> Please select {selectedSize} flavors</h2>

      <div className="grid-container">
        {flavors.map((source, index) => (
          <figure onClick={() => handleClick(index)} key={index}>
            <figcaption>{flavorName[index]}</figcaption>
            <img className="item" src={source} alt="맛 이미지" />
          </figure>
        ))}
      </div>
    </div>
  );
};

function ThirdPage({ selectedSize }) {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          You choose <Choose selectedSize={selectedSize} />
        </h1>
        <Menu selectedSize={selectedSize} />
      </header>
    </div>
  );
}

export default ThirdPage;
