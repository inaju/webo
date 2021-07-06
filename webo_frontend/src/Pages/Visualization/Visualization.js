import React from 'react'
import Filterbar from '../../Components/Sidebar/Filterbar'
import Sidebar from '../../Components/Sidebar/Sidebar'
import './Visualization.css'
import Chart from 'react-apexcharts'
import Piechart from '../../Components/Piechart'
import Linechart from '../../Components/Linechart'

function Visualization() {

    return (
        <div className="visualization-page">
            <Sidebar/>

            <div className="main-visualization">
                <Piechart/>
                <Piechart/>
                <Piechart/>
                <Piechart/>
                <Piechart/>
                <Piechart/>
            </div>

            <Filterbar/>

        </div>
    )
}

export default Visualization
