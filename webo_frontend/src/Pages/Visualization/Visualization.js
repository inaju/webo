import React, { useState, useEffect } from "react";
import Filterbar from "../../Components/Sidebar/Filterbar";
import Sidebar from "../../Components/Sidebar/Sidebar";
import "./Visualization.css";
import Chart from "react-apexcharts";
import Piechart from "../../Components/Piechart";
import Linechart from "../../Components/Linechart";
import LinechartComponent from "../../Components/LinechartComponent";

import Barchart from "../../Components/Barchart";
// import HorizontalBarChart from "../../Components/Horizontalbar";
import GroupedBar from "../../Components/Groupedbar";
import Horizontalbarchart from "../../Components/Horizontalbarchart";

function Visualization({
  document_type_x_value,
  document_type_y_value,
  author_x_value,
  author_y_value,
  open_access_x_value,
  open_access_y_value,
  affliation_x_value,
  affliation_y_value,
  sponsor_x_value,
  sponsor_y_value,
  data,
}) {
  return (
    <div className="visualization-page">
      {/* <Sidebar /> */}

      <div className="main-visualization">
        <div className="chart">
          <h3>Document Type</h3>
          <Piechart
            document_type_x={document_type_x_value}
            document_type_y={document_type_y_value}
          />
        </div>

        <div className="chart">
          <h3>Top Authors</h3>

          <Horizontalbarchart
            author_x_value={author_x_value}
            author_y_value={author_y_value}
          />
        </div>

        <div className="chart">
          <h3>Open Access</h3>

          {/* <GroupedBar /> */}
          <Barchart
            open_access_x_value={open_access_x_value}
            open_access_y_value={open_access_y_value}
          />
        </div>

        <div className="chart">
          <h3>Top Institutions</h3>

          <Horizontalbarchart
            author_x_value={affliation_x_value}
            author_y_value={affliation_y_value}
          />
        </div>

        <div className="chart">
          <h3>Top Funding Sponsors</h3>

          <Piechart
            document_type_x={sponsor_x_value}
            document_type_y={sponsor_y_value}
          />
        </div>
      </div>
    </div>
  );
}

export default Visualization;
