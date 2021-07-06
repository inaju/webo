import React from 'react'
import Chart from 'react-apexcharts'

function Piechart({series, labels}) {

    const data = {
        series: [44, 55, 41, 17, 15],
        chartOptions: {
        labels: ['Apple', 'Mango', 'Orange', 'Watermelon'],
        responsive: [{
            breakpoint: undefined,
            options: {},
        }]

    }
}
    
        return (
            <div className="piechart-container">
                <Chart
                options={data.chartOptions}
                series={data.series}
                type="pie"
                // height="350%"
                // width="100%"
            />
            </div>
        )
    }

export default Piechart
