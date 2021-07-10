import React from "react";
import "./Tab.css";
import { Link } from "react-router-dom";

function Tab({ icon_item, tabname, link }) {
  return (
    <div className="tab-component">
      <Link exact to={link} className="link">
        {icon_item}
        <p>{tabname}</p>
      </Link>
    </div>
  );
}

export default Tab;
