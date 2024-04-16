import React from "react";

export const ThemeContext = React.createContext({
  currentTheme: "light",
  setCurrentTheme: (_theme: string) => {},
  colorPrimary: "#1677ff",
  setColorPrimary: (_color: string) => {},
});
