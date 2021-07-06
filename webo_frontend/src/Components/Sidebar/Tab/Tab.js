import React from 'react'
import './Tab.css'

function Tab({icon_item, tabname, link}) {
    return (
        <div className="tab-component">
            <a href={link} className="link">
            {icon_item}
            <p>{tabname}</p>
            </a>
        </div>
    )
}

export default Tab
