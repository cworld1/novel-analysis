import React, { useState } from "react";
import { ConfigProvider as AntdConfigProvider, theme } from "antd";

// Config context
const initialContext = {
  currentTheme: sessionStorage.getItem("currentTheme") || "light",
  setCurrentTheme: (_theme: string) => {},
  colorPrimary: sessionStorage.getItem("colorPrimary") || "#1677ff",
  setColorPrimary: (_color: string) => {},
  serverAddress:
    sessionStorage.getItem("serverAddress") || "http://127.0.0.1:5000",
  setServerAddress: (_address: string) => {},
};

export const ConfigContext = React.createContext(initialContext);

export const ConfigProvider = ({ children }: { children: React.ReactNode }) => {
  const [currentTheme, _setCurrentTheme] = useState(
    initialContext.currentTheme
  );
  const [colorPrimary, _setColorPrimary] = useState(
    initialContext.colorPrimary
  );
  const [serverAddress, _setServerAddress] = useState(
    initialContext.serverAddress
  );

  // 更新函数同时将数据存入sessionStorage
  const setCurrentTheme = (value: string) => {
    sessionStorage.setItem("currentTheme", value);
    _setCurrentTheme(value);
  };

  const setColorPrimary = (value: string) => {
    sessionStorage.setItem("colorPrimary", value);
    _setColorPrimary(value);
  };

  const setServerAddress = (value: string) => {
    sessionStorage.setItem("serverAddress", value);
    _setServerAddress(value);
  };

  return (
    <ConfigContext.Provider
      value={{
        currentTheme,
        setCurrentTheme,
        colorPrimary,
        setColorPrimary,
        serverAddress,
        setServerAddress,
      }}
    >
      <AntdConfigProvider
        theme={{
          algorithm:
            currentTheme === "follow_system"
              ? window.matchMedia &&
                window.matchMedia("(prefers-color-scheme: dark)").matches
                ? theme.darkAlgorithm
                : theme.defaultAlgorithm
              : currentTheme === "dark"
              ? theme.darkAlgorithm
              : theme.defaultAlgorithm,
          token: {
            colorPrimary: colorPrimary,
          },
        }}
      >
        {children}
      </AntdConfigProvider>
    </ConfigContext.Provider>
  );
};
