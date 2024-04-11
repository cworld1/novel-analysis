import React, { useContext } from "react";

import {
  Button,
  Space,
  Input,
  ColorPicker,
  Divider,
  Switch,
  theme,
} from "antd";
import { ThemeContext } from "../components/ThemeProvider";

const SettingsPage: React.FC = () => {
  const { currentTheme, setCurrentTheme } = useContext(ThemeContext);
  return (
    <>
      {/* <ColorPicker showText value={color} onChangeComplete={} /> */}
      <Divider />
      <Space>
        <Switch
          checked={currentTheme === "dark"}
          onChange={(checked) => setCurrentTheme(checked ? "dark" : "light")}
        />
      </Space>
      <Divider />
      <Space>
        <Input placeholder="Please Input" />
        <Button type="primary">Submit</Button>
      </Space>
    </>
  );
};

export default SettingsPage;
