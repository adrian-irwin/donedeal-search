import MinMaxOption from "@/app/search/MinMaxOption";
import {
    maxEnginePowers,
    maxEngineSizes,
    maxMileages,
    maxPrices,
    maxSeats,
    maxYears,
    minEnginePowers,
    minEngineSizes,
    minMileages,
    minPrices,
    minSeats,
    minYears,
} from "@/app/search/utils";

export default function RangeSearches({ body, setBody }) {
    return (
        <div className="flex flex-col items-center justify-center text-center px-2">
            {/* Year Options */}
            <MinMaxOption
                body={body}
                setBody={setBody}
                minSetValue="min_year"
                maxSetValue="max_year"
                minData={minYears(body)}
                maxData={maxYears(body)}
                minPlaceholder="Min Year"
                maxPlaceholder="Max Year"
                minValue={body.range_filters.min_year}
                maxValue={body.range_filters.max_year}
            />

            {/* Price Options */}
            <MinMaxOption
                body={body}
                setBody={setBody}
                minSetValue="min_price"
                maxSetValue="max_price"
                minData={minPrices(body)}
                maxData={maxPrices(body)}
                minPlaceholder="Min Price"
                maxPlaceholder="Max Price"
                minValue={body.range_filters.min_price}
                maxValue={body.range_filters.max_price}
            />

            {/* Mileage Options */}
            <MinMaxOption
                body={body}
                setBody={setBody}
                minSetValue="min_mileage"
                maxSetValue="max_mileage"
                minData={minMileages(body)}
                maxData={maxMileages(body)}
                minPlaceholder="Min Mileage"
                maxPlaceholder="Max Mileage"
                minValue={body.range_filters.min_mileage}
                maxValue={body.range_filters.max_mileage}
            />

            {/* Engine Size Options */}
            <MinMaxOption
                body={body}
                setBody={setBody}
                minSetValue="min_engine"
                maxSetValue="max_engine"
                minData={minEngineSizes(body)}
                maxData={maxEngineSizes(body)}
                minPlaceholder="Min Engine Size"
                maxPlaceholder="Max Engine Size"
                minValue={body.range_filters.min_engine}
                maxValue={body.range_filters.max_engine}
            />

            {/* Engine Power Options */}
            <MinMaxOption
                body={body}
                setBody={setBody}
                minSetValue="min_enginePower"
                maxSetValue="max_enginePower"
                minData={minEnginePowers(body)}
                maxData={maxEnginePowers(body)}
                minPlaceholder="Min Engine Power"
                maxPlaceholder="Max Engine Power"
                minValue={body.range_filters.min_enginePower}
                maxValue={body.range_filters.max_enginePower}
            />

            {/* Seats Options */}
            <MinMaxOption
                body={body}
                setBody={setBody}
                minSetValue="min_seats"
                maxSetValue="max_seats"
                minData={minSeats(body)}
                maxData={maxSeats(body)}
                minPlaceholder="Min Seats"
                maxPlaceholder="Max Seats"
                minValue={body.range_filters.min_seats}
                maxValue={body.range_filters.max_seats}
            />

            {/* TODO: Add max road tax */}
        </div>
    );
}
