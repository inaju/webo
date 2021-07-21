import React from "react";
import "./Linechart.css";
import Chart from "react-apexcharts";

function Linechart({ x_value, y_value }) {
  const data = {
    options: {
      responsive: [
        {
          breakpoint: undefined,
          options: {
            width: "100%",
            height: "100%",
          },
        },
      ],
      fill: {
        type: "gradient",
        gradient: {
          shadeIntensity: 0.8,
          opacityFrom: 0.7,
          opacityTo: 0.95,
          stops: [0, 90, 100],
        },
      },
      chart: {
        id: "basic-bar",

        zoom: {
          enabled: false,
          type: "x",
          autoScaleYaxis: false,

          zoomedArea: {
            fill: {
              colors: "#09a2e4",
              opacity: 0.4,
            },

            stroke: {
              color: "#09a2e4",
              opacity: 0.2,
              width: 0.3,
            },
          },
        },
      },
      xaxis: {
        categories: x_value,
      },
      stroke: {
        curve: "smooth",
      },
    },

    series: [
      {
        name: "series-1",
        data: y_value,
      },
    ],
  };

  return (
    <div className="linechart-container">
      <Chart
        options={data.options}
        series={data.series}
        type="area"
        height="150%"
        width="100%"
      />
    </div>
  );
}

export default Linechart;
