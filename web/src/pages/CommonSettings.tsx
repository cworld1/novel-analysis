import React, { useContext } from "react";
// Antd
import { Button, ColorPicker, List, Select, Typography } from "antd";
const { Title } = Typography;
// Components
import { ThemeContext, ServerContext } from "../components/SettingsContext";
import {
  BgColorsOutlined,
  DeleteOutlined,
  ReloadOutlined,
  SkinOutlined,
} from "@ant-design/icons";

const SettingsPage: React.FC = () => {
  const { currentTheme, setCurrentTheme, colorPrimary, setColorPrimary } =
    useContext(ThemeContext);

  const appearanceData = [
    {
      title: "Primary color",
      avatar: <BgColorsOutlined style={{ fontSize: 27, height: 48 }} />,
      desc: "Change the primary color of the application",
      actions: [
        <ColorPicker
          showText
          value={colorPrimary}
          onChangeComplete={(color) => setColorPrimary(color.toHex())}
        />,
      ],
    },
    {
      title: "Color scheme",
      avatar: <SkinOutlined style={{ fontSize: 27, height: 48 }} />,
      desc: "Change the color scheme of the application",
      actions: [
        <Select
          style={{ width: 140 }}
          defaultValue={currentTheme}
          onChange={setCurrentTheme}
          options={[
            { value: "light", label: "Light" },
            { value: "dark", label: "Dark" },
            { value: "follow_system", label: "Follow system" },
          ]}
        />,
      ],
    },
  ];

  const databaseData = [
    {
      title: "Update database",
      avatar: <ReloadOutlined style={{ fontSize: 27, height: 48 }} />,
      desc: "Update the database schema to the latest version",
      actions: [
        <Button>Update force</Button>,
        <Button type="primary">Update</Button>,
      ],
    },
    {
      title: "Clear darabase",
      avatar: <DeleteOutlined style={{ fontSize: 27, height: 48 }} />,
      desc: "Clear the database and reset to the default state",
      actions: [<Button danger>Clear</Button>],
    },
  ];

  const renderListItem = (item: any) => (
    <List.Item actions={item.actions}>
      <List.Item.Meta
        avatar={item.avatar}
        title={item.title}
        description={item.desc}
      />
    </List.Item>
  );

  return (
    <>
      <Title>Settings</Title>
      <Title level={4}>Appearance</Title>
      <List
        bordered
        itemLayout="horizontal"
        dataSource={appearanceData}
        renderItem={renderListItem}
      />
      <Title level={4}>Database</Title>
      <List
        bordered
        itemLayout="horizontal"
        dataSource={databaseData}
        renderItem={renderListItem}
      />
    </>
  );
};

export default SettingsPage;
