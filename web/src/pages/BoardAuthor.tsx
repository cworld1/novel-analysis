import React, { useEffect } from "react";
// Antd
import { Spin, theme, Typography } from "antd";
const { Title, Paragraph } = Typography;
// Echarts
import axios from "axios";
import * as echarts from "echarts";

const BoardAuthorPage: React.FC = () => {
  const {
    token: { colorFillQuaternary, borderRadiusLG },
  } = theme.useToken();

  const getImage = async (shape: string) => {
    axios
      .get(`http://127.0.0.1:5000/anal/author?shape=${shape}`)
      .then(function (result) {
        var chart = echarts.init(document.getElementById(shape), "white", {
          renderer: "canvas",
        });
        chart.setOption(result.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  useEffect(() => {
    const fetchData = async () => {
      getImage("bar");
      // getImage("pie");
    };

    fetchData();
  }, []);

  const chartStyle = {
    maxWidth: 1000,
    height: 500,
    padding: 25,
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: colorFillQuaternary,
    borderRadius: borderRadiusLG,
  };

  return (
    <>
      <Title>Type of novel</Title>
      <Paragraph>
        <div id="bar" style={chartStyle}>
          <Spin />
        </div>
      </Paragraph>
      {/* <Paragraph>
        <div id="pie" style={chartStyle}>
          <Spin />
        </div>
      </Paragraph> */}
    </>
  );
};

export default BoardAuthorPage;
