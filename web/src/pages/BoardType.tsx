import React, { useContext, useEffect } from "react";
// Antd
import { Spin, theme, Typography } from "antd";
const { Title, Paragraph } = Typography;
// Echarts
import axios from "axios";
import * as echarts from "echarts";
import { ConfigContext } from "../components/ConfigProvider";

const BoardTypePage: React.FC = () => {
  const {
    token: { colorFillQuaternary, borderRadiusLG },
  } = theme.useToken();
  const { serverAddress } = useContext(ConfigContext);

  const getImage = async (shape: string) => {
    axios
      .get(`${serverAddress}/anal/type?shape=${shape}`)
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
      getImage("pie");
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
      <Title>Type of Novel</Title>
      <Paragraph>
        <div id="bar" style={chartStyle}>
          <Spin />
        </div>
      </Paragraph>
      <Paragraph>
        <div id="pie" style={chartStyle}>
          <Spin />
        </div>
      </Paragraph>
    </>
  );
};

export default BoardTypePage;
