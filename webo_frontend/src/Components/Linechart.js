import React from 'react'
import './Linechart.css';
import Chart from 'react-apexcharts'

function Linechart() {
    const data={
    options: {
      responsive: [{
        breakpoint: undefined,
        options: {
          width: '100%',
          height:'100%'
        },
    }],
        chart: {
          id: "basic-bar",
          fill: {
            colors: 'red',
            opacity: 0.4
          },


          zoom: {
            enabled: false,
            type: 'x',  
            autoScaleYaxis: false,  

            zoomedArea: {
              fill: {
                colors: '#09a2e4',
                opacity: 0.4
              },

              stroke: {
                color: '#09a2e4',
                opacity: 0.2,
                width: 1,
              }

            }

        }


        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002]
        },
        stroke: {
            curve: 'smooth',
          }
      },


      series: [
        {
          name: "series-1",
          data: [30, 40, 45, 50, 49, 60, 70, 91, 60, 40, 45]
        }
      ]


    }

    return (
        <div className="linechart-container">
            <Chart
            options={data.options}
            series={data.series}
            type="line"
            height="150%"
            width="100%"
        />
        </div>
    )
}

export default Linechart
