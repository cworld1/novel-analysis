import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
// Antd
import { ReloadOutlined } from "@ant-design/icons";
import { FloatButton } from "antd";
// Components
import { ConfigContext } from "../components/ConfigProvider";

interface FloatButtonsProps {
  messageApi: any;
}

const FloatButtons: React.FC<FloatButtonsProps> = ({ messageApi }) => {
  const key = "updatable";
  const [refreshing, setRefreshing] = useState(false);
  const [startPolling, setStartPolling] = useState(false); // Add this state
  const { serverAddress } = useContext(ConfigContext);

  // Trigger data refreshing
  const handleRefreshClick = () => {
    messageApi.open({
      key,
      type: "loading",
      content: "Refreshing data...",
      duration: 0,
    });
    axios
      .get(`${serverAddress}/crawl/refresh`)
      .then(() => {
        setStartPolling(true); // Start polling after clicked refresh button
      })
      .catch((err) => console.log(err));
  };

  /// Poll refresh status every 5 seconds, if startPolling is true
  useEffect(() => {
    let interval = null;
    if (startPolling) {
      interval = setInterval(() => {
        axios
          .get(`${serverAddress}/crawl/refresh-status`)
          .then((res) => {
            setRefreshing(res.data.status);
            if (res.data.status === false) {
              // Stop polling when status is false
              messageApi.open({
                key,
                type: "success",
                content: "Data refreshed",
                duration: 2,
              });
              setStartPolling(false);
            }
          })
          .catch((err) => console.log(err));
      }, 1000);
    }
    return () => {
      if (interval) {
        clearInterval(interval); // Clean up on unmount
      }
    };
  }, [startPolling]); // Rerun the effect if startPolling state changes

  return (
    <FloatButton.Group shape="circle" style={{ right: 24 }}>
      <FloatButton.BackTop visibilityHeight={300} />
      <FloatButton
        icon={<ReloadOutlined spin={refreshing} />}
        type="primary"
        tooltip={<div>Reload</div>}
        onClick={handleRefreshClick}
      />
    </FloatButton.Group>
  );
};

export default FloatButtons;
