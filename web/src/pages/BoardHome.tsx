import React, { useState, useEffect } from "react";
import axios from "axios";
// Antd
import { Card, Carousel, Col, Row } from "antd";
const { Meta } = Card;

interface BookInfo {
  bookName: string;
  authorName: string;
}

const BoardHomePage: React.FC = () => {
  const bookCount = 12;
  const [books, setBooks] = useState<Array<BookInfo>>(
    Array(bookCount).fill({ bookName: "", authorName: "" })
  );
  const [images, setImages] = useState<string[]>(Array(bookCount).fill(""));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const bookUrl = `http://127.0.0.1:5000/fetch/novel?choose=random&count=${bookCount}`;
    axios
      .get<BookInfo[]>(bookUrl)
      .then((response) => {
        setBooks(response.data);
        setLoading(false);
      })
      .catch((error) => console.error("Error:", error));

    const imageUrl = `http://127.0.0.1:5000/fetch/cover?count=${bookCount}`;
    axios
      .get<string[]>(imageUrl)
      .then((response) => {
        setImages(response.data);
        setLoading(false);
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
      <Row justify="space-evenly" gutter={[16, 16]}>
        {books &&
          books.map((book, index) => (
            <Col
              xs={{ span: 12 }}
              sm={{ span: 10 }}
              md={{ span: 8 }}
              lg={{ span: 6 }}
              xl={{ span: 4 }}
              key={index}
            >
              <Card
                hoverable
                style={{ width: "100%" }}
                cover={
                  images && images[index] ? (
                    <img
                      alt={`cover${index}`}
                      src={`data:image/jpeg;base64,${images[index]}`}
                    />
                  ) : null
                }
                loading={loading}
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
