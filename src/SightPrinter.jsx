import React from 'react';

export const SightPrinter = (props) => {
    const {city} = props;

    const haveCity = city !== "null";
    return (
        haveCity && <div>
            {city}
        </div>
    );
}