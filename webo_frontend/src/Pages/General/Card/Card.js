import React from 'react'
import './Card.css';

function Card({title,value}) {
    return (
        <div className="card-component">
           
            <div className="card-icon">

            </div>

            <div className="card-content">
                <h3>
                    {title}
                </h3>

                <p>
                    {value}
                </p>

            </div>
        </div>
    )
}

export default Card
