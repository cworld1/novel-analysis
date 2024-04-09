import React, { useEffect, useState } from "react";
import axios from "axios";

const getImage = async (shape: string) => {
  const response = await axios.get(
    `http://127.0.0.1:5000/plot/type?shape=${shape}`,
    {
      responseType: "arraybuffer",
    }
  );

  const base64 = btoa(
    new Uint8Array(response.data).reduce(
      (data, byte) => data + String.fromCharCode(byte),
      ""
    )
  );
  return "data:;base64," + base64;
};

const BoardTypePage: React.FC = () => {
  const [barImage, setBarImage] = useState("");
  const [pieImage, setPieImage] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      const barImg = await getImage("bar");
      const pieImg = await getImage("pie");
      setBarImage(barImg);
      setPieImage(pieImg);
    };

    fetchData();
  }, []);

  return (
    <>
      <h2>Type of novel</h2>
      {barImage && <img src={barImage} alt="Novel type bar" />}
      {pieImage && <img src={pieImage} alt="Novel type pie" />}
    </>
  );
};

export default BoardTypePage;
