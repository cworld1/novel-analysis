import React from "react";
// Antd
import { Typography, Layout, Card, Row, Col, Button, Flex } from "antd";
import { Link } from "react-router-dom";
const { Title, Paragraph } = Typography;
const { Content, Footer } = Layout;
// Assets
import reactLogo from "../assets/react.svg";

const HomePage: React.FC = () => (
  <Layout style={{ padding: "0 40px" }}>
    <Content>
      <Flex
        justify="space-between"
        className="banner"
        style={{ padding: "100px 0" }}
      >
        <div className="banner-left">
          <Flex vertical>
            <Title>Novel Analysis Project</Title>
            <Paragraph>
              Retrieve and analyze info from novels published on the Hongxiu
              Novel Website.
            </Paragraph>
          </Flex>
          <div className="banner-buttons">
            <Link to="/board">
              <Button type="primary" style={{ marginRight: "10px" }}>
                Browse Dashboard
              </Button>
            </Link>
            <Link to="/about">
              <Button type="default">About Us</Button>
            </Link>
          </div>
        </div>
        <Flex className="banner-right" style={{ margin: "0 40px" }}>
          <img
            src={reactLogo}
            className="logo react"
            alt="React logo"
            width={100}
          />
        </Flex>
      </Flex>
      <Row gutter={16}>
        <Col xs={24} md={12}>
          <Card bordered={false}>
            <Paragraph>
              We aim to provide insights into corresponding literature; from
              revealing overarching trends to delineating intricate narrative
              structures, that would otherwise go unnoticed.
            </Paragraph>
          </Card>
        </Col>
        <Col xs={24} md={12}>
          <Card>
            <Paragraph>
              Please browse around and feel free to provide us with feedback.
              Let's embark on this literary journey together!
            </Paragraph>
          </Card>
        </Col>
      </Row>
    </Content>
    {/* Footer */}
    <Footer style={{ textAlign: "center" }}>
      Ant Design ©{new Date().getFullYear()} Created by Ant UED
    </Footer>
  </Layout>
);

export default HomePage;
