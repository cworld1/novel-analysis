import React from "react";
// Antd
import { Breadcrumb, Layout, theme } from "antd";
// Components
import { routeItems } from "../components/Routes";

const { Content, Footer } = Layout;

interface CommonTemplateProps {
  PageContent: React.ElementType;
}

const CommonTemplate: React.FC<CommonTemplateProps> = ({ PageContent }) => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  return (
    <Layout className="site-layout">
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
        Ant Design ©{new Date().getFullYear()} Created by Ant UED
      </Footer>
    </Layout>
  );
};

export default CommonTemplate;
