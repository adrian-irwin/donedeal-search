"use client";

import { MantineProvider } from "@mantine/core";
import { useState } from "react";
import { SearchDataContext } from "@/app/contexts/SearchDataContext";

export default function Providers({ children }) {
    const [body, setBody] = useState({
        main_filters: {
            sellerType: [],
            fuelType: [],
            transmission: [],
            bodyType: [],
            numDoors: [],
            colour: [],
            country: [],
        },
        make_model_filters: {},
        range_filters: {
            min_year: "",
            max_year: "",
            min_price: "",
            max_price: "",
            min_mileage: "",
            max_mileage: "",
            min_engine: "",
            max_engine: "",
            min_enginePower: "",
            max_enginePower: "",
            min_seats: "",
            max_seats: "",
            max_roadTax: "",
        },
    });

    return (
        <SearchDataContext.Provider value={{ body, setBody }}>
            <MantineProvider defaultColorScheme="dark">
                {children}
            </MantineProvider>
        </SearchDataContext.Provider>
    );
}
