import React from "react";
import { Bar } from "react-chartjs-2";
import "./Barchart.css";

function Barchart({ open_access_x_value, open_access_y_value }) {
  const chart_data = {
    labels: open_access_x_value,
    datasets: [
      {
        label: "Rainfall",
        backgroundColor: "#09A2E4",
        borderColor: "#09A2E4",
        borderWidth: 1,
        data: open_access_y_value,
      },
    ],
  };

  return (
    <div className="barchart-container">
      <Bar
        data={chart_data}
        options={{
          title: {
            display: true,
            text: "Average Rainfall per month",
            fontSize: 20,
          },
          legend: {
            display: true,
            position: "right",
          },
        }}
        height={"150%"}
        // width={"500px"}
      />
    </div>
  );
}

export default Barchart;
