import React, { useState, useEffect } from "react";
import Dropdown from "react-dropdown";

import "./App.css";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import General from "./Pages/General/General";
import Analysis from "./Pages/Analysis/Analysis";
import Visualization from "./Pages/Visualization/Visualization";

function App() {
  const [x_value, setX_value] = useState([]);
  const [y_value, set_Yvalue] = useState([]);
  const [number_of_paper, setNumber_of_paper] = useState([]);
  const [number_of_citations, setNumber_of_citations] = useState([]);
  const [author_per_paper, setAuthor_per_paper] = useState([]);

  const [document_type_x_value, setDocument_type_X_value] = useState([]);
  const [document_type_y_value, setDocument_type_Y_value] = useState([]);

  const [author_x_value, setAuthor_X_value] = useState([]);
  const [author_y_value, setAuthor_Y_value] = useState([]);

  const [open_access_x_value, setOpen_access_X_value] = useState([]);
  const [open_access_y_value, setOpen_access_Y_value] = useState([]);

  const [affliation_x_value, setAffliation_X_value] = useState([]);
  const [affliation_y_value, setAffliation_Y_value] = useState([]);

  const [data, setData] = useState([]);

  useEffect(() => {
    const data = "Communications And Networking";

    fetch("http://127.0.0.1:8000/api/v1/generalpageapi/post/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((results) => results.json())
      .then((data) => {
        // const { name } = data.results[0];
        console.log(data["x"]);
        setX_value(data["x"]);
        set_Yvalue(data["y"]);
        setNumber_of_paper(data["number_of_papers"]);
        setNumber_of_citations(data["number_of_citations"]);
        setAuthor_per_paper(data["author_per_paper"]);

        setDocument_type_X_value(data["document_type"]["x"]);
        setDocument_type_Y_value(data["document_type"]["y"]);

        setAuthor_X_value(data["author_frequency"]["x"]);
        setAuthor_Y_value(data["author_frequency"]["y"]);

        setOpen_access_X_value(data["open_access"]["x"]);
        setOpen_access_Y_value(data["open_access"]["y"]);

        setAffliation_X_value(data["affliation_response"]["x"]);
        setAffliation_Y_value(data["affliation_response"]["y"]);
        console.log(data["document_type"]["x"], data["document_type"]["y"]);
      });
  }, []);

  const onChange = (e) => {
    console.log(e.value);
    const data = e.value;

    fetch("http://127.0.0.1:8000/api/v1/generalpageapi/post/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((results) => results.json())
      .then((data) => {
        // const { name } = data.results[0];
        console.log(data["x"]);
        setX_value(data["x"]);
        set_Yvalue(data["y"]);
        setNumber_of_paper(data["number_of_papers"]);
        setNumber_of_citations(data["number_of_citations"]);
        setAuthor_per_paper(data["author_per_paper"]);

        setDocument_type_X_value(data["document_type"]["x"]);
        setDocument_type_Y_value(data["document_type"]["y"]);

        setAuthor_X_value(data["author_frequency"]["x"]);
        setAuthor_Y_value(data["author_frequency"]["y"]);

        setOpen_access_X_value(data["open_access"]["x"]);
        setOpen_access_Y_value(data["open_access"]["y"]);

        setAffliation_X_value(data["affliation_response"]["x"]);
        setAffliation_Y_value(data["affliation_response"]["y"]);
        console.log(data["document_type"]["x"], data["document_type"]["y"]);
      });
  };

  const options = [
    "Internet Of Things",
    "Communications And Networking",
    "Electrical Machines",
    "Induction Motors",
  ];
  const defaultOption = options[1];

  return (
    <div className="App">
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

      <Switch>
        <div className="app-component">
          <Route path="/" exact>
            <General
              x_value={x_value}
              y_value={y_value}
              number_of_paper={number_of_paper}
              number_of_citations={number_of_citations}
              author_per_paper={author_per_paper}
            />
          </Route>
          <Route path="/analysis" component={Analysis} />

          <Route path="/visualization" exact>
            <Visualization
              document_type_x_value={document_type_x_value}
              document_type_y_value={document_type_y_value}
              author_x_value={author_x_value}
              author_y_value={author_y_value}
              open_access_x_value={open_access_x_value}
              open_access_y_value={open_access_y_value}
              affliation_x_value={affliation_x_value}
              affliation_y_value={affliation_y_value}
              data={data}
            />
          </Route>
          <Route path="/visualization" component={Visualization} />
        </div>
      </Switch>
    </div>
  );
}

export default App;
