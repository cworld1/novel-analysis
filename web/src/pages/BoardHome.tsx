import React, { useState, useEffect } from "react";
import axios from "axios";
// Antd
import { Alert, Card, Carousel, Col, Row, Typography } from "antd";
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

// Banner interface
interface BannerInfo {
  id: string;
  link: string;
  description: string;
}
interface BannerCarouselProps {
  bannerinfos: BannerInfo[];
}

// Custom component for displaying carousel
const BannerCarousel: React.FC<BannerCarouselProps> = ({ bannerinfos }) => (
  <Carousel autoplay style={{ maxWidth: 900, minWidth: 800 }}>
    {/* <Carousel style={{ maxWidth: 900, minWidth: 800 }}> */}
    {bannerinfos.map((banner: BannerInfo, index: number) => (
      <div key={index}>
        <a
          href={banner.link}
          style={{
            display: "block",
            background: "#364d79",
            position: "relative",
          }}
        >
          <img
            style={{ maxWidth: "100%" }}
            src={`http://127.0.0.1:5000/fetch/banner?id=${banner.id}`}
            alt={banner.description}
          />
          <p
            style={{
              position: "absolute",
              bottom: 0,
              padding: "20px 0 25px",
              margin: 0,
              width: "100%",
              textAlign: "center",
              color: "white",
              background:
                "linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, .6))",
            }}
          >
            {banner.description}
          </p>
        </a>
      </div>
    ))}
  </Carousel>
);

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
  // Init banner states
  const [banners, setBanners] = useState<Array<BannerInfo>>(
    Array(5).fill({ id: "", link: "", description: "" })
  );
  // Init book states
  const bookCount = 12;
  const [books, setBooks] = useState<Array<BookInfo>>(
    Array(bookCount).fill({ bookName: "", authorName: "" })
  );
  const [bookImages, setBookImages] = useState<string[]>(
    Array(bookCount).fill("")
  );
  const [bookLoading, setBookLoading] = useState(true);

  useEffect(() => {
    // Fetch banner info
    axios
      .get<BannerInfo[]>("http://127.0.0.1:5000/fetch/banners")
      .then((response) => {
        setBanners(response.data);
      });

    // Fetch book info
    const bookUrl = `http://127.0.0.1:5000/fetch/novel?choose=random&count=${bookCount}`;
    axios
      .get<BookInfo[]>(bookUrl)
      .then((response) => {
        setBooks(response.data);
        setBookLoading(false);
      })
      .catch((error) => console.error("Error:", error));

    // Fetch cover images
    const imageUrl = `http://127.0.0.1:5000/fetch/cover?count=${bookCount}`;
    axios
      .get<string[]>(imageUrl)
      .then((response) => {
        setBookImages(response.data);
        setBookLoading(false);
      })
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <>
      <Alert
        message="Data updated at Apr 16, Tuesday"
        type="success"
        showIcon
        closable
      />
      <Title>Board</Title>
      <div style={{ display: "flex", justifyContent: "center" }}>
        <BannerCarousel bannerinfos={banners} />
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
                image={bookImages ? bookImages[index] : ""}
                loading={bookLoading}
              />
            </Col>
          ))}
      </Row>
    </>
  );
};

export default BoardHomePage;
