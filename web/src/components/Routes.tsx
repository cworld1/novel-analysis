import React from "react";
import { Route, Routes, useLocation } from "react-router-dom";
// Pages
import HomePage from "../pages/Home";
import BoardPage from "../pages/Board";
import CommonPage from "../pages/Common";
import BoardHomePage from "../pages/BoardHome";
import SettingsPage from "../pages/CommonSettings";
import AboutPage from "../pages/CommonAbout";
import BoardTypePage from "../pages/BoardType";

export const RouteContent: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/board" element={<BoardPage />}>
        <Route path="/board" element={<BoardHomePage />} />
        <Route path="/board/type" element={<BoardTypePage />} />
      </Route>
      <Route
        path="/settings"
        element={<CommonPage PageContent={SettingsPage} />}
      />
      <Route path="/about" element={<CommonPage PageContent={AboutPage} />} />
    </Routes>
  );
};

export const routeMapping: { [key: string]: string } = {
  home: "Home",
  board: "Dashboard",
  type: "Type",
  settings: "Settings",
  about: "About",
};

export const routeItems = (): { title: string | JSX.Element }[] => {
  const location = useLocation();

  const paths = location.pathname.split("/").filter(Boolean);

  const items = ["home", ...paths]
    .map((path, index) => {
      const title = routeMapping[path];
      if (!title) {
        return undefined;
      }

      if (path === "home") {
        return { title: <a href="/">{title}</a> };
      } else if (index < paths.length) {
        const href = "/" + paths.slice(0, index).join("/");
        return { title: <a href={href}>{title}</a> };
      } else {
        return { title: title };
      }
    })
    .filter(Boolean);

  return items as { title: string | JSX.Element }[];
};
