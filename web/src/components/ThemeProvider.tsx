import React, { useState } from "react";
import { ConfigProvider, theme } from "antd";
import { MapToken } from "antd/es/theme/interface";

export const ThemeContext = React.createContext({
  currentTheme: "light",
  setCurrentTheme: (_theme: "light" | "dark") => {},
});

export interface ThemeState {
  currentTheme: MapToken;
}

export const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const [currentTheme, setCurrentTheme] = useState<"light" | "dark">("light");

  return (
    <ThemeContext.Provider value={{ currentTheme, setCurrentTheme }}>
      <ConfigProvider
        theme={{
          algorithm:
            currentTheme === "light"
              ? theme.defaultAlgorithm
              : theme.darkAlgorithm,
        }}
      >
        {children}
      </ConfigProvider>
    </ThemeContext.Provider>
  );
};
