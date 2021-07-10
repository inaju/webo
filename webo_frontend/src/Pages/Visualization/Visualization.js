import React from "react";
import Filterbar from "../../Components/Sidebar/Filterbar";
import Sidebar from "../../Components/Sidebar/Sidebar";
import "./Visualization.css";
import Chart from "react-apexcharts";
import Piechart from "../../Components/Piechart";
import Linechart from "../../Components/Linechart";
import LinechartComponent from "../../Components/LinechartComponent";

import Barchart from "../../Components/Barchart";
import HorizontalBarChart from "../../Components/Horizontalbar";
import GroupedBar from "../../Components/Groupedbar";
function Visualization() {
  return (
    <div className="visualization-page">
      <Sidebar />

      <div className="main-visualization">
        <div className="line-chart">
          <h3>Document By Year</h3>

          <Piechart />
        </div>
        <div className="line-chart">
          <h3>Document By Year</h3>

          <HorizontalBarChart />
        </div>
        <div className="line-chart">
          <h3>Document By Year</h3>

          <LinechartComponent />
        </div>
        <div className="line-chart">
          <h3>Document By Year</h3>

          <GroupedBar />
        </div>
        <div className="line-chart">
          <h3>Document By Year</h3>

          <Piechart />
        </div>
        <div className="line-chart">
          <h3>Document By Year</h3>

          <Barchart />
        </div>
      </div>

      <Filterbar />
    </div>
  );
}

export default Visualization;
