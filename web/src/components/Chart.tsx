import { Spin, theme } from "antd";
import ReactEcharts from "echarts-for-react";

interface ChartProps {
  option: any;
}

const ChartComponent: React.FC<ChartProps> = ({ option }) => {
  const {
    token: { colorFillQuaternary, borderRadiusLG },
  } = theme.useToken();

  const chartStyle = {
    maxWidth: 1000,
    height: 500,
    padding: 25,
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: colorFillQuaternary,
    borderRadius: borderRadiusLG,
  };
  return (
    <div style={chartStyle}>
      {option ? (
        <ReactEcharts
          option={option}
          style={{ width: "100%", height: "100%" }}
        />
      ) : (
        <Spin />
      )}
    </div>
  );
};

export default ChartComponent;
