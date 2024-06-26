import React, { useContext, useState } from "react";
// Antd
import {
  Button,
  ColorPicker,
  Input,
  List,
  message,
  Select,
  Typography,
} from "antd";
const { Title } = Typography;
// Components
import { ConfigContext } from "../components/ConfigProvider";
import {
  BgColorsOutlined,
  CloudServerOutlined,
  DeleteOutlined,
  ReloadOutlined,
  SkinOutlined,
} from "@ant-design/icons";

const SettingsPage: React.FC = () => {
  const key = "updatable";
  const {
    currentTheme,
    setCurrentTheme,
    colorPrimary,
    setColorPrimary,
    serverAddress,
    setServerAddress,
  } = useContext(ConfigContext);
  // save address input for setting content of setaddress
  const [inputValue, setInputValue] = useState(serverAddress);
  const [messageApi, contextHolder] = message.useMessage();

  const openMessage = () => {
    messageApi.open({
      key,
      type: "loading",
      content: "Loading...",
    });
    setTimeout(() => {
      messageApi.open({
        key,
        type: "success",
        content: "Loaded!",
        duration: 2,
      });
    }, 1000);
  };

  const serverData = [
    {
      title: "Server address",
      avatar: <CloudServerOutlined style={{ fontSize: 27, height: 48 }} />,
      desc: "Change the address of the local data server",
      actions: [
        <Input
          allowClear
          placeholder="http://127.0.0.1:5000"
          value={inputValue}
          onChange={(event) => setInputValue(event.target.value)}
          onBlur={() => {
            setServerAddress(inputValue);
          }}
        />,
      ],
    },
  ];

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
        <Button onClick={openMessage}>Update force</Button>,
        <Button type="primary" onClick={openMessage}>
          Update
        </Button>,
      ],
    },
    {
      title: "Clear darabase",
      avatar: <DeleteOutlined style={{ fontSize: 27, height: 48 }} />,
      desc: "Clear the database and reset to the default state",
      actions: [
        <Button danger onClick={openMessage}>
          Clear
        </Button>,
      ],
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
      {contextHolder}
      <Title>Settings</Title>
      <Title level={4}>Server</Title>
      <List
        bordered
        itemLayout="horizontal"
        dataSource={serverData}
        renderItem={renderListItem}
      />
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
