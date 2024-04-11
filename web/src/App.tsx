import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
// Antd
import { FloatButton, Layout, theme } from "antd";
const { Header } = Layout;
// Components
import TopAppBar from "./components/TopAppBar";
import { RouteContent } from "./components/Routes";
import { ReloadOutlined } from "@ant-design/icons";

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
          <RouteContent />
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
