import React, { useEffect } from "react";
import axios from "axios";
import * as echarts from "echarts";

const getImage = async (shape: string) => {
  var chart = echarts.init(document.getElementById(shape), "white", {
    renderer: "canvas",
  });
  axios
    .get(`http://127.0.0.1:5000/plot/type?shape=${shape}`)
    .then(function (result) {
      chart.setOption(result.data);
    })
    .catch(function (error) {
      console.log(error);
    });
};

const BoardTypePage: React.FC = () => {
  useEffect(() => {
    const fetchData = async () => {
      await getImage("bar");
      await getImage("pie");
    };

    fetchData();
  }, []);

  return (
    <>
      <h2>Type of novel</h2>
      <div id="bar" style={{ width: 1000, height: 600 }} />
      <div id="pie" style={{ width: 1000, height: 600 }} />
    </>
  );
};

export default BoardTypePage;
