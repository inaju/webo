import React from "react";
import "./Sidebar.css";
import Tab from "./Tab/Tab.js";

import { RiDashboardLine } from "react-icons/ri";
import { RiAccountCircleLine } from "react-icons/ri";
import { RiPieChartLine } from "react-icons/ri";
import { AiOutlineLineChart } from "react-icons/ai";
import { FiLogOut } from "react-icons/fi";

function Sidebar() {
  return (
    <div className="sidebar-container">
      <div className="account">
        <Tab
          icon_item={<RiAccountCircleLine size={30} className="icon" />}
          link={"/account"}
          tabname={"Mitchel"}
        />
      </div>

      <div className="real_tabs">
        <Tab
          icon_item={<RiDashboardLine size={30} className="icon general" />}
          link={"/"}
          tabname={"General"}
        />
        <Tab
          icon_item={
            <RiPieChartLine size={30} className="icon visualization" />
          }
          link={"/visualization"}
          tabname={"Visualization"}
        />
        <Tab
          icon_item={<AiOutlineLineChart size={30} className="icon analysis" />}
          link={"/analysis"}
          tabname={"Analysis"}
        />
      </div>

      <div className="logout">
        <Tab icon_item={<FiLogOut className="icon" />} tabname={"Logout"} />
      </div>
    </div>
  );
}

export default Sidebar;
