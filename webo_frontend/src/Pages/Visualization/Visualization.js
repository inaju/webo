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
  data,
}) {
  // const [document_type_x_value, setDocument_type_X_value] = useState([]);
  // const [document_type_y_value, setDocument_type_Y_value] = useState([]);

  // const [author_x_value, setAuthor_X_value] = useState([]);
  // const [author_y_value, setAuthor_Y_value] = useState([]);

  // const [open_access_x_value, setOpen_access_X_value] = useState([]);
  // const [open_access_y_value, setOpen_access_Y_value] = useState([]);

  // const [affliation_x_value, setAffliation_X_value] = useState([]);
  // const [affliation_y_value, setAffliation_Y_value] = useState([]);

  // const [data, setData] = useState([]);
  // // const [number_of_citations, setNumber_of_citations] = useState([]);
  // // const [author_per_paper, setAuthor_per_paper] = useState([]);

  // useEffect(() => {
  //   fetch("http://127.0.0.1:8000/api/v1/visualizationpageapi/")
  //     .then((results) => results.json())
  //     .then((data) => {
  //       setDocument_type_X_value(data["x"]);
  //       setDocument_type_Y_value(data["y"]);

  //       setAuthor_X_value(data["author_frequency"]["x"]);
  //       setAuthor_Y_value(data["author_frequency"]["y"]);

  //       setOpen_access_X_value(data["open_access"]["x"]);
  //       setOpen_access_Y_value(data["open_access"]["y"]);

  //       setAffliation_X_value(data["affliation_response"]["x"]);
  //       setAffliation_Y_value(data["affliation_response"]["y"]);
  //     });
  // }, []);
  // console.log(document_type_x_value, document_type_y_value);
  return (
    <div className="visualization-page">
      <Sidebar />

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
          <h3>Document By Year</h3>

          <LinechartComponent />
        </div>
        <div className="chart">
          <h3>Document By Year</h3>

          <Piechart
            document_type_x={document_type_x_value}
            document_type_y={document_type_y_value}
            datachart={data}
          />
        </div>
        <div className="chart">
          <h3>Document By Year</h3>

          <Barchart />
        </div>
      </div>

      {/* <Filterbar /> */}
    </div>
  );
}

export default Visualization;
