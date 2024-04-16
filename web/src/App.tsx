import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
// Antd
import { FloatButton, Layout } from "antd";
import { ReloadOutlined } from "@ant-design/icons";
// Components
import TopAppBar from "./components/TopAppBar";
import { RouteContent } from "./components/Routes";
import { ConfigProvider } from "./components/ConfigProvider";

const App: React.FC = () => {
  return (
    <Router>
      <ConfigProvider>
        <Layout style={{ minHeight: "100vh" }}>
          {/* Header */}
          <TopAppBar />
          {/* Contents */}
          <div style={{ marginTop: 64 }}>
            <RouteContent />
          </div>
        </Layout>
        {/* Float button */}
        <FloatButton.Group shape="circle" style={{ right: 24 }}>
          <FloatButton.BackTop visibilityHeight={300} />
          <FloatButton
            icon={<ReloadOutlined />}
            type="primary"
            tooltip={<div>Reload</div>}
          />
        </FloatButton.Group>
      </ConfigProvider>
    </Router>
  );
};

export default App;
