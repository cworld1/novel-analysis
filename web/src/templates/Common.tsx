import React from "react";
// Antd
import { Breadcrumb, Layout, theme } from "antd";
const { Content, Footer } = Layout;
// Components
import { routeItems } from "../components/Routes";

interface CommonTemplateProps {
  PageContent: React.ElementType;
}

const CommonTemplate: React.FC<CommonTemplateProps> = ({ PageContent }) => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  return (
    <Layout
      className="site-layout"
      style={{ maxWidth: 1200, margin: "0 auto" }}
    >
      {/* Content */}
      <Layout style={{ padding: "0 48px" }}>
        <Breadcrumb style={{ margin: "16px 0" }} items={routeItems()} />
        <Content
          style={{
            background: colorBgContainer,
            minHeight: 280,
            padding: 24,
            borderRadius: borderRadiusLG,
          }}
        >
          <PageContent />
        </Content>
      </Layout>
      {/* Footer */}
      <Footer style={{ textAlign: "center" }}>
        Data Analysis ©{new Date().getFullYear()} Created by CWorld
      </Footer>
    </Layout>
  );
};

export default CommonTemplate;
