import React from "react";
import { Breadcrumb, Layout, theme } from "antd";

const { Content, Footer } = Layout;

interface CommonPageProps {
  PageContent: React.ElementType;
}

const CommonPage: React.FC<CommonPageProps> = ({ PageContent }) => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  return (
    <Layout className="site-layout">
      {/* Content */}
      <Layout style={{ padding: "0 48px" }}>
        <Breadcrumb style={{ margin: "16px 0" }}>
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item>List</Breadcrumb.Item>
          <Breadcrumb.Item>App</Breadcrumb.Item>
        </Breadcrumb>
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

export default CommonPage;
