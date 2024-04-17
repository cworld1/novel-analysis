import React, { ReactNode, useContext, useEffect, useState } from "react";
// Antd
import { Collapse, CollapseProps, Spin, theme, Typography } from "antd";
const { Title, Paragraph } = Typography;
// Echarts
import axios from "axios";
import * as echarts from "echarts";
import "echarts-wordcloud";
// Components
import { ConfigContext } from "../components/ConfigProvider";
import Typewriter from "../components/TypeWriter";

const BoardAuthorPage: React.FC = () => {
  const {
    token: { colorFillQuaternary, borderRadiusLG },
  } = theme.useToken();
  const { serverAddress } = useContext(ConfigContext);

  // Get different images
  const getImage = async (shape: string) => {
    axios
      .get(`${serverAddress}/anal/comment?shape=${shape}`)
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
      getImage("wordcloud");
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

  const items: CollapseProps["items"] = [
    {
      key: "1",
      label: "This is panel header 1",
      children: (
        <Typewriter>
          <p>Hello world</p>
          <p>Hello world 2</p>
        </Typewriter>
      ),
    },
    {
      key: "2",
      label: "This is panel header 2",
      children: <p>Hello world</p>,
    },
  ];

  const onChange = (key: string | string[]) => {
    console.log(key);
  };

  return (
    <>
      <Title>Type of Comment</Title>
      <Paragraph>
        <div id="wordcloud" style={chartStyle}>
          <Spin />
        </div>
      </Paragraph>
      <Title level={4}>AI Analysis of Novels</Title>
      <Collapse items={items} defaultActiveKey={["1"]} onChange={onChange} />
    </>
  );
};

export default BoardAuthorPage;
