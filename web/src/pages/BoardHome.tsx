import React, { useState, useEffect } from "react";
import axios from "axios";
// Ant design
import { Card, Carousel, Col, Row } from "antd";
const { Meta } = Card;

interface BookInfo {
  bookName: string;
  authorName: string;
}

const BoardHomePage: React.FC = () => {
  const [books, setBooks] = useState<BookInfo[] | null>(null);
  const bookCount = 3;

  useEffect(() => {
    const url = `http://127.0.0.1:5000/fetch/novel?choose=random&count=${bookCount}`;
    axios
      .get<BookInfo[]>(url)
      .then((response) => {
        setBooks(response.data);
      })
      .catch((error) => console.error("Error:", error));
  }, []);

  const contentStyle: React.CSSProperties = {
    height: "300px",
    color: "#fff",
    lineHeight: "300px",
    textAlign: "center",
    background: "#364d79",
    marginBottom: "0",
  };
  return (
    <>
      <h2>Board</h2>
      <Row gutter={16}>
        {books &&
          books.map((book, index) => (
            <Col span={8} key={index}>
              <Card
                hoverable
                style={{ width: 240 }}
                cover={
                  <img
                    alt="example"
                    src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
                  />
                }
              >
                <Meta title={book.bookName} description={book.authorName} />
              </Card>
            </Col>
          ))}
      </Row>
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
};

export default BoardHomePage;
