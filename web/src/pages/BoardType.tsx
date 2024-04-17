import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
// Antd
import { Typography } from "antd";
const { Title, Paragraph } = Typography;
// Components
import { ConfigContext } from "../components/ConfigProvider";
import ChartComponent from "../components/Chart";

const BoardTypePage: React.FC = () => {
  const [bar, setBar] = useState();
  const [pie, setPie] = useState();
  const { serverAddress } = useContext(ConfigContext);

  const getImage = async (shape: string) => {
    return axios
      .get(`${serverAddress}/anal/type?shape=${shape}`)
      .then((res) => res.data);
  };

  useEffect(() => {
    const fetchData = async () => {
      getImage("bar").then((data) => setBar(data));
      getImage("pie").then((data) => setPie(data));
    };

    fetchData();
  }, []);

  return (
    <>
      <Title>Type of Novel</Title>
      <Paragraph>
        <ChartComponent option={bar} />
      </Paragraph>
      <Paragraph>
        <ChartComponent option={pie} />
      </Paragraph>
    </>
  );
};

export default BoardTypePage;
