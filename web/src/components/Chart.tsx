import { Spin, theme } from "antd";
import ReactEcharts from "echarts-for-react";

interface ChartProps {
  option: any;
  width?: number;
  height?: number | string;
  forceWidth?: boolean;
}

const ChartComponent: React.FC<ChartProps> = ({
  option,
  width = 1000,
  height = 500,
  forceWidth = false,
}) => {
  const {
    token: { colorFillQuaternary, borderRadiusLG },
  } = theme.useToken();

  const chartStyle = {
    width: width,
    height: height,
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
          style={{ width: forceWidth ? width - 50 : "100%", height: "100%" }}
        />
      ) : (
        <Spin />
      )}
    </div>
  );
};

export default ChartComponent;
