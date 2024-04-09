import React from "react";
import { To, useNavigate } from "react-router-dom";
// Ant design
import { Menu, MenuProps } from "antd";
import {
  UploadOutlined,
  UserOutlined,
  VideoCameraOutlined,
} from "@ant-design/icons";
// Assets
import reactLogo from "../assets/react.svg";

const Sidebar: React.FC = () => {
  const navigate = useNavigate();
  const handleClick = (route: To) => {
    navigate(route);
  };

  const items: MenuProps["items"] = [
    {
      key: "1",
      icon: <UserOutlined />,
      label: "Home",
      onClick: () => handleClick("/"),
    },
    { type: "divider" },
    {
      key: "2",
      icon: <VideoCameraOutlined />,
      label: "Settings",
      onClick: () => handleClick("/settings"),
    },
    {
      key: "3",
      icon: <UploadOutlined />,
      label: "About",
      onClick: () => handleClick("/about"),
    },
  ];

  return (
    <>
      <div
        className="header"
        style={{
          display: "flex",
          alignItems: "center",
          padding: "18px 19px 11px",
        }}
      >
        <div className="logo">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </div>
        <span className="title" style={{ marginLeft: "12px" }}>
          React
        </span>
      </div>
      <Menu mode="inline" defaultSelectedKeys={["1"]} items={items} />
    </>
  );
};

export default Sidebar;
