import React from "react";
import { Route, Routes } from "react-router-dom";
// Pages
import HomePage from "../pages/Home";
import BoardPage from "../pages/Board";
import CommonPage from "../pages/Common";
import BoardHomePage from "../pages/BoardHome";
import SettingsPage from "../pages/CommonSettings";
import AboutPage from "../pages/CommonAbout";
import BoardTypePage from "../pages/BoardType";

const RouteContents: React.FC = () => {
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

export default RouteContents;
