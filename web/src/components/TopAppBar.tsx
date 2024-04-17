import React from "react";
import { To, useNavigate, useLocation } from "react-router-dom";
// Antd
import { Flex, Menu, MenuProps, theme, Layout, Button, Tooltip } from "antd";
const { Header } = Layout;
// Assets
import reactLogo from "../assets/react.svg";
import { GithubOutlined } from "@ant-design/icons";

const TopAppBar: React.FC = () => {
  // React router
  const navigate = useNavigate();
  const getKey = () => "/" + (location.pathname.split("/")[1] || "");
  const location = useLocation();
  const handleClick = (route: To) => {
    navigate(route);
  };
  // Theme color
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  // Menu items
  const items: MenuProps["items"] = [
    {
      key: "/",
      label: "Home",
      onClick: () => handleClick("/"),
    },
    {
      key: "/board",
      label: "Dashboard",
      onClick: () => handleClick("/board"),
    },
    {
      key: "/settings",
      label: "Settings",
      onClick: () => handleClick("/settings"),
    },
    {
      key: "/about",
      label: "About",
      onClick: () => handleClick("/about"),
    },
  ];

  return (
    <Header
      style={{
        display: "flex",
        alignItems: "center",
        background: colorBgContainer,
        padding: "0 34px",
        position: "fixed",
        left: 0,
        right: 0,
        zIndex: 1,
      }}
    >
      <Flex className="logo" style={{ width: 200 - 34 }}>
        <img src={reactLogo} className="logo react" alt="React logo" />
        <span className="title" style={{ marginLeft: "10px" }}>
          React
        </span>
      </Flex>
      <Menu
        mode="horizontal"
        selectedKeys={[getKey()]}
        defaultSelectedKeys={[getKey()]}
        items={items}
      ></Menu>
      <div style={{ flex: 1, textAlign: "end" }}>
        <Tooltip placement="bottom" title="Github">
          <Button
            type="text"
            icon={<GithubOutlined />}
            onClick={() =>
              window.open("https://github.com/cworld1/novel_analysis", "_blank")
            }
          />
        </Tooltip>
      </div>
    </Header>
  );
};

export default TopAppBar;
