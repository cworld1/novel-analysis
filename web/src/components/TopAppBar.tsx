import React from "react";
import { To, useNavigate, useLocation } from "react-router-dom";
// Antd
import { Flex, Menu, MenuProps, theme, Layout } from "antd";
const { Header } = Layout;
// Assets
import reactLogo from "../assets/react.svg";

const TopAppBar: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const handleClick = (route: To) => {
    navigate(route);
  };
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  const routeToKey: Record<string, string> = {
    "/": "1",
    "/board": "2",
    "/settings": "3",
    "/about": "4",
  };
  const items: MenuProps["items"] = [
    {
      key: "1",
      label: "Home",
      onClick: () => handleClick("/"),
    },
    {
      key: "2",
      label: "Dashboard",
      onClick: () => handleClick("/board"),
    },
    {
      key: "3",
      label: "Settings",
      onClick: () => handleClick("/settings"),
    },
    {
      key: "4",
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
        selectedKeys={[routeToKey[location.pathname]]}
        defaultSelectedKeys={[routeToKey[location.pathname]]}
        items={items}
        style={{ flex: 1, minWidth: 0 }}
      ></Menu>
    </Header>
  );
};

export default TopAppBar;
