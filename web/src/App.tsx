import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
// Ant design
import { FloatButton, Layout, theme } from "antd";
// Components
import TopAppBar from "./components/TopAppBar";
import RouteContents from "./components/Routes";
import { ReloadOutlined } from "@ant-design/icons";

const { Header } = Layout;

const App: React.FC = () => {
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  return (
    <Router>
      <Layout>
        {/* Header */}
        <Header
          style={{
            display: "flex",
            alignItems: "center",
            background: colorBgContainer,
            padding: "0 24px",
            position: "fixed",
            left: 0,
            right: 0,
            zIndex: 1,
          }}
        >
          <TopAppBar />
        </Header>
        {/* Contents */}
        <div style={{ marginTop: 64 }}>
          <RouteContents />
        </div>
      </Layout>
      <FloatButton.Group shape="circle" style={{ right: 24 }}>
        <FloatButton.BackTop visibilityHeight={0} />
        <FloatButton
          icon={<ReloadOutlined />}
          type="primary"
          tooltip={<div>Reload</div>}
        />
      </FloatButton.Group>
    </Router>
  );
};

export default App;
