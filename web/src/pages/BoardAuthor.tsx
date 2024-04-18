import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
// Antd
import { Typography } from "antd";
const { Title, Paragraph } = Typography;
// Components
import { ConfigContext } from "../components/ConfigProvider";
import ChartComponent from "../components/Chart";

const BoardAuthorPage: React.FC = () => {
  const [bar, setBar] = useState();
  const [heatmap, setHeatmap] = useState();
  const { serverAddress } = useContext(ConfigContext);

  const getImage = async (shape: string) => {
    return axios
      .get(`${serverAddress}/anal/author?shape=${shape}`)
      .then((res) => res.data);
  };

  useEffect(() => {
    const fetchData = async () => {
      getImage("bar").then((data) => setBar(data));
      getImage("heatmap").then((data) => setHeatmap(data));
    };

    fetchData();
  }, []);

  return (
    <>
      <Title>Author of Novel</Title>
      <Paragraph>
        <ChartComponent option={bar} />
      </Paragraph>
      <Paragraph>
        <ChartComponent option={heatmap} />
      </Paragraph>
    </>
  );
};

export default BoardAuthorPage;
