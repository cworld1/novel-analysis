import React from "react";
import { To, useNavigate, useLocation } from "react-router-dom";
// Ant design
import { Menu, MenuProps } from "antd";
import {
  AppstoreOutlined,
  CommentOutlined,
  DashboardOutlined,
  UsergroupAddOutlined,
  UserOutlined,
} from "@ant-design/icons";

const Sidebar: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const handleClick = (route: To) => {
    navigate(route);
  };

  const routeToKey: Record<string, string> = {
    "/board": "1",
    "/board/type": "2",
    "/board/author": "3",
    "/board/comment": "4",
    "/board/character": "5",
  };
  const items: MenuProps["items"] = [
    {
      key: "1",
      icon: <DashboardOutlined />,
      label: "Dashboard",
      onClick: () => handleClick("/board"),
    },
    { type: "divider" },
    {
      key: "2",
      icon: <AppstoreOutlined />,
      label: "Type",
      onClick: () => handleClick("/board/type"),
    },
    {
      key: "3",
      icon: <UserOutlined />,
      label: "Author",
      onClick: () => handleClick("/board/author"),
    },
    {
      key: "4",
      icon: <CommentOutlined />,
      label: "Comment",
      onClick: () => handleClick("/board/comment"),
    },
    {
      key: "5",
      icon: <UsergroupAddOutlined />,
      label: "Character",
      onClick: () => handleClick("/board/character"),
    },
  ];

  return (
    <Menu defaultSelectedKeys={[routeToKey[location.pathname]]} items={items} />
  );
};

export default Sidebar;
