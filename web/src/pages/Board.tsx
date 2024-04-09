import React, { useState } from "react";
import { Breadcrumb, Layout, theme } from "antd";
// Components
import Sidebar from "../components/Sidebar";
import { Outlet } from "react-router-dom";

const { Sider, Content, Footer } = Layout;

const BoardPage: React.FC = () => {
  const [collapsed, setCollapsed] = useState(false);
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  return (
    <Layout style={{ minHeight: "100vh" }}>
      {/* Sidebar */}
      <Sider
        collapsible
        collapsed={collapsed}
        onCollapse={(value) => setCollapsed(value)}
        width={200}
        style={{
          overflow: "auto",
          height: "100vh",
          position: "fixed",
          left: 0,
          top: 64,
          bottom: 0,
          background: colorBgContainer,
        }}
      >
        <Sidebar />
      </Sider>
      <Layout
        style={{
          marginLeft: collapsed ? 80 : 200,
          padding: "0 24px 24px",
          transition: "margin-left 0.22s",
        }}
      >
        {/* Breadcrumb */}
        <Breadcrumb style={{ margin: "16px 0" }}>
          <Breadcrumb.Item>User</Breadcrumb.Item>
          <Breadcrumb.Item>Bill</Breadcrumb.Item>
        </Breadcrumb>
        <Content
          style={{
            background: colorBgContainer,
            minHeight: 280,
            padding: 24,
            borderRadius: borderRadiusLG,
          }}
        >
          <Outlet />
        </Content>
        {/* Footer */}
        <Footer style={{ textAlign: "center" }}>
          Ant Design ©{new Date().getFullYear()} Created by Ant UED
        </Footer>
      </Layout>
    </Layout>
  );
};

export default BoardPage;
