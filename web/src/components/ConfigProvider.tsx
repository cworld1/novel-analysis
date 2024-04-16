import React, { useState } from "react";
import { ConfigProvider as AntdConfigProvider, theme } from "antd";

// Config context
export const ConfigContext = React.createContext({
  currentTheme: "light",
  setCurrentTheme: (_theme: string) => {},
  colorPrimary: "#1677ff",
  setColorPrimary: (_color: string) => {},
  serverAddress: "http://127.0.0.1:5000",
  setServerAddress: (_address: string) => {},
});

export const ConfigProvider = ({ children }: { children: React.ReactNode }) => {
  const [currentTheme, setCurrentTheme] = useState("light");
  const [colorPrimary, setColorPrimary] = useState("#1677ff");
  const [serverAddress, setServerAddress] = useState("http://127.0.0.1:5000");

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
