import React from "react";
// Ant design
import { Carousel } from "antd";

const contentStyle: React.CSSProperties = {
  height: "300px",
  color: "#fff",
  lineHeight: "300px",
  textAlign: "center",
  background: "#364d79",
  marginBottom: "0",
};

const HomePage: React.FC = () => (
  <>
    <h2>Home</h2>
    <Carousel autoplay style={{ maxWidth: "650px" }}>
      <div>
        <h3 style={contentStyle}>1</h3>
      </div>
      <div>
        <h3 style={contentStyle}>2</h3>
      </div>
      <div>
        <h3 style={contentStyle}>3</h3>
      </div>
      <div>
        <h3 style={contentStyle}>4</h3>
      </div>
    </Carousel>
  </>
);

export default HomePage;
