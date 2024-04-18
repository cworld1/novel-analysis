import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
// Antd
import { Button, Collapse, CollapseProps, Typography } from "antd";
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

  const getImage = async (shape: string) => {
    return axios
      .get(`${serverAddress}/anal/comment?shape=${shape}`)
      .then((res) => res.data);
  };
  useEffect(() => {
    const fetchData = async () => {
      getImage("wordcloud").then((data) => setWordcloud(data));
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

  const items: CollapseProps["items"] = books?.map((book, index) => {
    return {
      key: String(index),
      label: book.bookName,
      children: [
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
        </Paragraph>,
      ],
      extra: <Text type="secondary">{book.authorName}</Text>,
    };
  });

  // const onChange = (key: string | string[]) => {
  //   console.log(key);
  // };

  return (
    <>
      <Title>Comment of Novel</Title>
      <Paragraph>
        <ChartComponent option={wordcloud} />
      </Paragraph>
      <Title level={4}>AI Analysis of Novels</Title>
      <Collapse
        items={items}
        defaultActiveKey={["1"]}
        // onChange={onChange}
      />
    </>
  );
};

export default BoardAuthorPage;
