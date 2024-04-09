import React from "react";
// Ant design
import { Menu, MenuProps } from "antd";
// Assets
import reactLogo from "../assets/react.svg";
import { To, useNavigate } from "react-router-dom";

const TopAppBar: React.FC = () => {
  const navigate = useNavigate();
  const handleClick = (route: To) => {
    navigate(route);
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
    <div
      style={{
        display: "flex",
        alignItems: "center",
        padding: 10,
        width: "100%",
      }}
    >
      <div className="logo" style={{ display: "flex", width: 200 - 24 - 10 }}>
        <img src={reactLogo} className="logo react" alt="React logo" />
        <span className="title" style={{ marginLeft: "10px" }}>
          React
        </span>
      </div>
      <Menu
        mode="horizontal"
        defaultSelectedKeys={["2"]}
        items={items}
        style={{ flex: 1, minWidth: 0 }}
      ></Menu>
    </div>
  );
};

export default TopAppBar;
