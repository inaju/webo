import React from "react";
import { Bar } from "react-chartjs-2";

function Horizontalbarchart({ author_x_value, author_y_value }) {
  const data = {
    labels: author_x_value,
    datasets: [
      {
        label: "Authors",
        data: author_y_value,
        backgroundColor: ["#09A2E4"],
        borderWidth: 0,
      },
    ],
  };

  const options = {
    height: "100%",
    indexAxis: "y",
    // Elements options apply to all of the options unless overridden in a dataset
    // In this case, we are setting the border of each horizontal bar to be 2px wide
    elements: {
      bar: {
        borderWidth: 2,
      },
    },
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        position: "right",
      },
    },
  };

  return (
    <div className="horizontalbar_container">
      <Bar data={data} width={"95%"} height={"75%"} options={options} />
    </div>
  );
}

export default Horizontalbarchart;
