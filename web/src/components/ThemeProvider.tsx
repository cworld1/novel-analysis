import React, { useState } from "react";
import { ConfigProvider, theme } from "antd";
// Components
import { ThemeContext } from "./SettingsContext";

export const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const [currentTheme, setCurrentTheme] = useState<string>("light");
  const [colorPrimary, setColorPrimary] = useState<string>("#1677ff");

  return (
    <ThemeContext.Provider
      value={{ currentTheme, setCurrentTheme, colorPrimary, setColorPrimary }}
    >
      <ConfigProvider
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
      </ConfigProvider>
    </ThemeContext.Provider>
  );
};
