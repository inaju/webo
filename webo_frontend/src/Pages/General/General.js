import React, { useState, useEffect } from "react";

import "./General.css";
import Dropdown from "react-dropdown";
import "react-dropdown/style.css";
import Card from "./Card/Card";
import Sidebar from "../../Components/Sidebar/Sidebar";
import Filterbar from "../../Components/Sidebar/Filterbar";
import Linechart from "../../Components/Linechart";
import LinechartComponenet from "../../Components/LinechartComponent";
import DataTableNew from "../../Components/TableNew";
import DataTable from "../../Components/Table";

function General() {
  const [x_value, setX_value] = useState([]);
  const [y_value, set_Yvalue] = useState([]);
  const [number_of_paper, setNumber_of_paper] = useState([]);
  const [number_of_citations, setNumber_of_citations] = useState([]);
  const [author_per_paper, setAuthor_per_paper] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/generalpageapi/")
      .then((results) => results.json())
      .then((data) => {
        // const { name } = data.results[0];
        console.log(data["x"]);
        setX_value(data["x"]);
        set_Yvalue(data["y"]);
        setNumber_of_paper(data["number_of_papers"]);
        setNumber_of_citations(data["number_of_citations"]);
        setAuthor_per_paper(data["author_per_paper"]);
      });
  }, []);

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
          <Card title="Number Of Papers" value={number_of_paper} />
          <Card title="Citation Per Paper" value={number_of_citations} />
          <Card title="Author Per Paper" value={author_per_paper} />
        </div>

        <div className="line-chart">
          <h3>Document By Year</h3>

          <Linechart x_value={x_value} y_value={y_value} />
        </div>

        <div className="table">
          <DataTable />
        </div>
      </div>

      <Filterbar />
    </div>
  );
}

export default General;
