import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
// Antd
import { Layout, message } from "antd";
// Components
import TopAppBar from "./components/TopAppBar";
import { RouteContent } from "./components/Routes";
import { ConfigProvider } from "./components/ConfigProvider";
import FloatButtons from "./components/FloatButton";

const App: React.FC = () => {
  const [messageApi, contextHolder] = message.useMessage();

  return (
    <Router>
      <ConfigProvider>
        <Layout style={{ minHeight: "100vh" }}>
          {contextHolder}
          {/* Header */}
          <TopAppBar />
          {/* Contents */}
          <div style={{ marginTop: 64 }}>
            <RouteContent />
          </div>
        </Layout>
        {/* Float button */}
        <FloatButtons messageApi={messageApi} />
      </ConfigProvider>
    </Router>
  );
};

export default App;
