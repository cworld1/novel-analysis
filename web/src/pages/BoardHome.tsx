import React, { useState, useEffect } from "react";
import axios from "axios";
// Antd
import { Card, Carousel, Col, Row, Typography } from "antd";
import { ArrowRightOutlined } from "@ant-design/icons";
const { Meta } = Card;
const { Title } = Typography;

// Book interface
interface BookInfo {
  bookName: string;
  authorName: string;
}
interface BookCardProps {
  book: BookInfo;
  image: string;
  loading: boolean;
}

// Custom component for displaying book cards
const BookCard: React.FC<BookCardProps> = ({ book, image, loading }) => (
  <Card
    hoverable
    style={{
      width: "100%",
      display: "flex",
      overflow: "hidden",
      justifyContent: "space-between",
    }}
    cover={
      image ? (
        <img
          alt="cover"
          style={{ width: 90, height: 120, objectFit: "cover" }}
          src={`data:image/jpeg;base64,${image}`}
        />
      ) : null
    }
    loading={loading}
    actions={[<ArrowRightOutlined style={{ paddingRight: 15 }} key="go" />]}
  >
    <Meta title={book.bookName} description={book.authorName} />
  </Card>
);

const BoardHomePage: React.FC = () => {
  // Init basic infos and states
  const bookCount = 12;
  const [books, setBooks] = useState<Array<BookInfo>>(
    Array(bookCount).fill({ bookName: "", authorName: "" })
  );
  const [images, setImages] = useState<string[]>(Array(bookCount).fill(""));
  const [loading, setLoading] = useState(true);

  // Fetch book info and cover images
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
      <Title>Board</Title>
      <div style={{ display: "flex", justifyContent: "center" }}>
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
      </div>
      <Title level={4}>Recommend Novel Shelves</Title>
      <Row justify="space-evenly" gutter={[16, 16]}>
        {books &&
          books.map((book, index) => (
            <Col
              xs={{ span: 12 }}
              sm={{ span: 10 }}
              md={{ span: 8 }}
              lg={{ span: 6 }}
              xl={{ span: 8 }}
              key={index}
            >
              <BookCard
                book={book}
                image={images ? images[index] : ""}
                loading={loading}
              />
            </Col>
          ))}
      </Row>
    </>
  );
};

export default BoardHomePage;
