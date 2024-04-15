import React from "react";
import { To, useNavigate, useLocation } from "react-router-dom";
// Antd
import { Menu, MenuProps } from "antd";
import {
  AppstoreOutlined,
  CommentOutlined,
  DashboardOutlined,
  UsergroupAddOutlined,
  UserOutlined,
} from "@ant-design/icons";

const Sidebar: React.FC = () => {
  // React router
  const navigate = useNavigate();
  const getKey = () => "/" + (location.pathname.split("/")[2] || "");
  const location = useLocation();
  const handleClick = (route: To) => {
    navigate(route);
  };

  // Menu items
  const items: MenuProps["items"] = [
    {
      key: "/",
      icon: <DashboardOutlined />,
      label: "Dashboard",
      onClick: () => handleClick("/board"),
    },
    { type: "divider" },
    {
      key: "/type",
      icon: <AppstoreOutlined />,
      label: "Type",
      onClick: () => handleClick("/board/type"),
    },
    {
      key: "/author",
      icon: <UserOutlined />,
      label: "Author",
      onClick: () => handleClick("/board/author"),
    },
    {
      key: "/comment",
      icon: <CommentOutlined />,
      label: "Comment",
      onClick: () => handleClick("/board/comment"),
    },
    {
      key: "/character",
      icon: <UsergroupAddOutlined />,
      label: "Character",
      onClick: () => handleClick("/board/character"),
    },
  ];

  return (
    <Menu
      selectedKeys={[getKey()]}
      defaultSelectedKeys={[getKey()]}
      items={items}
    />
  );
};

export default Sidebar;
