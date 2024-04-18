import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
// Antd
import { Button, Collapse, CollapseProps, Flex, Typography } from "antd";
const { Title, Paragraph, Text } = Typography;
import { ArrowRightOutlined } from "@ant-design/icons";
// Echart
import "echarts-wordcloud";
// Components
import { ConfigContext } from "../components/ConfigProvider";
import Typewriter from "../components/TypeWriter";
import ChartComponent from "../components/Chart";

// Book interface
interface BookInfo {
  bookId: string;
  bookName: string;
  authorName: string;
  comments: string[];
}

const getImage = async (serverAddress: string, shape: string) => {
  return axios
    .get(`${serverAddress}/anal/comment?shape=${shape}`)
    .then((res) => res.data);
};

const Card: React.FC<BookInfo> = (book) => {
  const [pie, setPie] = useState();
  const [line, setLine] = useState();
  const { serverAddress } = useContext(ConfigContext);

  useEffect(() => {
    const fetchData = async () => {
      getImage(serverAddress, "pie").then((data) => setPie(data));
      getImage(serverAddress, "line").then((data) => setLine(data));
    };
    fetchData();
  }, []);

  return (
    <>
      <Title level={4}>Comment Analysis</Title>
      <Flex>
        <ChartComponent option={pie} width={500} height={350} />
        <ChartComponent option={line} width={500} height={350} />
      </Flex>
      <Title level={4}>AI Comment</Title>
      <Typewriter texts={book.comments}></Typewriter>,
      <Paragraph>
        {book.bookId != "" && (
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
        )}
      </Paragraph>
    </>
  );
};

const BoardAuthorPage: React.FC = () => {
  const bookCount = 12;
  const [books, setBooks] = useState<Array<BookInfo>>(
    Array<BookInfo>(bookCount).fill({
      bookId: "",
      bookName: "",
      authorName: "",
      comments: [],
    })
  );
  const [wordcloud, setWordcloud] = useState();
  const { serverAddress } = useContext(ConfigContext);

  useEffect(() => {
    const fetchData = async () => {
      getImage(serverAddress, "wordcloud").then((data) => setWordcloud(data));
    };
    fetchData();

    // Fetch book info
    axios
      .get<BookInfo[]>(
        `${serverAddress}/fetch/novel?choose=random&count=${bookCount}`
      )
      .then((res) => {
        setBooks(res.data);
      });
  }, []);

  const items: CollapseProps["items"] = books?.map((book, index) => {
    return {
      key: String(index),
      label: book.bookName,
      children: <Card {...book} />,
      extra: <Text type="secondary">{book.authorName}</Text>,
    };
  });

  return (
    <>
      <Title>Comment of Novel</Title>
      <Paragraph>
        <ChartComponent option={wordcloud} />
      </Paragraph>
      <Title level={4}>AI Analysis of Novels</Title>
      <Collapse items={items} defaultActiveKey={["1"]} />
    </>
  );
};

export default BoardAuthorPage;
