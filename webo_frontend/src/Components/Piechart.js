import React from "react";
import Chart from "react-apexcharts";
import "./Piechart.css";
function Piechart({ document_type_x, document_type_y }) {
  // console.log(document_type_x, document_type_y);
  //   console.log(datachart);
  //   console.log(datachart)
  console.log(document_type_y);
  console.log(document_type_x);
  const data = {
    // series: datachart["y"],

    series: document_type_y,
    chartOptions: {
      labels: document_type_x,
      legend: {
        position: "bottom",
      },

      //   labels: datachart["x"],
      responsive: [
        {
          breakpoint: undefined,
          options: {},
        },
      ],
    },
  };

  return (
    <div className="piechart-container">
      <Chart
        options={data.chartOptions}
        series={data.series}
        type="pie"
        height="88%"
        width="95%"
        padding="50px"
      />
    </div>
  );
}

export default Piechart;
