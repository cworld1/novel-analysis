import React, { useState } from "react";
import { Outlet } from "react-router-dom";
// Antd
import { Breadcrumb, Layout, theme } from "antd";
const { Sider, Content, Footer } = Layout;
// Components
import Sidebar from "../components/Sidebar";
import { routeItems } from "../components/Routes";

const BoardTemplate: React.FC = () => {
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
          padding: "0 50px 50px",
          transition: "margin-left 0.22s",
        }}
      >
        {/* Breadcrumb */}
        <Breadcrumb
          style={{ margin: "16px 0" }}
          items={routeItems()}
        ></Breadcrumb>
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
          Data Analysis ©{new Date().getFullYear()} Created by CWorld
        </Footer>
      </Layout>
    </Layout>
  );
};

export default BoardTemplate;
