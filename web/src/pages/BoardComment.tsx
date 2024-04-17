import React, { useContext, useEffect, useState } from "react";
// Antd
import { Button, Collapse, CollapseProps, Spin, theme, Typography } from "antd";
const { Title, Paragraph, Text } = Typography;
// Echarts
import axios from "axios";
import * as echarts from "echarts";
import "echarts-wordcloud";
// Components
import { ConfigContext } from "../components/ConfigProvider";
import Typewriter from "../components/TypeWriter";
import { ArrowRightOutlined } from "@ant-design/icons";

// Book interface
interface BookInfo {
  bookId: string;
  bookName: string;
  authorName: string;
  comments: string[];
}

const BoardAuthorPage: React.FC = () => {
  const bookCount = 12;
  const {
    token: { colorFillQuaternary, borderRadiusLG },
  } = theme.useToken();
  const [books, setBooks] = useState<Array<BookInfo>>();
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
    };
    fetchData();

    // Fetch book info
    axios
      .get<BookInfo[]>(
        `${serverAddress}/fetch/novel?choose=random&count=${bookCount}`
      )
      .then((response) => {
        setBooks(response.data);
      });
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

  const items: CollapseProps["items"] = books?.map((book, index) => {
    return {
      key: String(index),
      label: book.bookName,
      children: [
        <Typewriter textArray={book.comments}></Typewriter>,
        <Paragraph>
          <Button
            onClick={() =>
              window.open(
                `https://www.hongxiu.com/book/${book.bookId}`,
                "_blank"
              )
            }
          >
            Read <ArrowRightOutlined />
          </Button>
        </Paragraph>,
      ],
      extra: <Text type="secondary">{book.authorName}</Text>,
    };
  });

  const onChange = (key: string | string[]) => {
    console.log(key);
  };

  return (
    <>
      <Title>Comment of Novel</Title>
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
