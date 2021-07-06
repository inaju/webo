import React from "react";
import "./General.css";
import Dropdown from "react-dropdown";
import "react-dropdown/style.css";
import Card from "./Card/Card";
import Sidebar from "../../Components/Sidebar/Sidebar";
import Filterbar from "../../Components/Sidebar/Filterbar";
import Linechart from "../../Components/Linechart";
import Table from "../../Components/Table";

function General() {
  const onChange = (e) => {
    console.log(e.value);
  };
  const options = [
    "Internet Of Things",
    "Electrical Machines",
    "Induction Motors",
  ];
  const defaultOption = options[0];

  return (
    <div className="general-component">
      <Sidebar />

      <div className="main-general">
        <div className="search-field">
          <Dropdown
            className="dropdown"
            options={options}
            onChange={onChange}
            value={defaultOption}
            placeholder="Select an option"
          />
          <button className="search-button">Search</button>
        </div>

        <div className="cards">
          <Card title="Number of papers" value="1000" />
          <Card title="Number of Citations" value="4000" />
          <Card title="H-Index" value="6.7" />
        </div>

        <div className="line-chart">
          <h3>Document Per Year</h3>

          <Linechart />
        </div>

        <div className="table">
          <Table />
        </div>
      </div>

      <Filterbar />
    </div>
  );
}

export default General;
