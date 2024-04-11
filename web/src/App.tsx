import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
// Antd
import { FloatButton, Layout } from "antd";
import { ReloadOutlined } from "@ant-design/icons";
// Components
import TopAppBar from "./components/TopAppBar";
import { RouteContent } from "./components/Routes";
import { ThemeProvider } from "./components/ThemeProvider";

const App: React.FC = () => {
  return (
    <Router>
      <ThemeProvider>
        <Layout>
          {/* Header */}
          <TopAppBar />
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
      </ThemeProvider>
    </Router>
  );
};

export default App;
