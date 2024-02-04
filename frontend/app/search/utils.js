import {
    enginePowers,
    engineSizes,
    mileages,
    prices,
    seats,
    years,
} from "@/app/search/data";

// Years

export function minYears(body) {
    const maxYear = body.range_filters.max_year
        ? parseInt(body.range_filters.max_year)
        : new Date().getFullYear();

    return years.filter((year) => year <= maxYear);
}

export function maxYears(body) {
    const minYear = body.range_filters.min_year
        ? parseInt(body.range_filters.min_year)
        : 1980;

    return years.filter((year) => year >= minYear);
}

// Prices

export function minPrices(body) {
    const maxPrice = body.range_filters.max_price
        ? parseInt(body.range_filters.max_price)
        : 100000;
    return prices.filter((price) => price.value <= maxPrice);
}

export function maxPrices(body) {
    const minPrice = body.range_filters.min_price
        ? parseInt(body.range_filters.min_price)
        : 0;
    return prices.filter((price) => price.value >= minPrice);
}

// Mileage (km)

export function minMileages(body) {
    const maxMileage = body.range_filters.max_mileage
        ? parseInt(body.range_filters.max_mileage)
        : 300000;
    return mileages.filter((mileage) => mileage.value <= maxMileage);
}

export function maxMileages(body) {
    const minMileage = body.range_filters.min_mileage
        ? parseInt(body.range_filters.min_mileage)
        : 0;
    return mileages.filter((mileage) => mileage.value >= minMileage);
}

// Engine Size

export function minEngineSizes(body) {
    const maxEngineSize = body.range_filters.max_engine
        ? parseInt(body.range_filters.max_engine)
        : 5000;
    return engineSizes.filter(
        (engineSize) => engineSize.value <= maxEngineSize,
    );
}

export function maxEngineSizes(body) {
    const minEngineSize = body.range_filters.min_engine
        ? parseInt(body.range_filters.min_engine)
        : 1000;
    return engineSizes.filter(
        (engineSize) => engineSize.value >= minEngineSize,
    );
}

// Engine Power

export function minEnginePowers(body) {
    const maxEnginePower = body.range_filters.max_enginePower
        ? parseInt(body.range_filters.max_enginePower)
        : 500;
    return enginePowers.filter(
        (enginePower) => enginePower.value <= maxEnginePower,
    );
}

export function maxEnginePowers(body) {
    const minEnginePower = body.range_filters.min_enginePower
        ? parseInt(body.range_filters.min_enginePower)
        : 0;
    return enginePowers.filter(
        (enginePower) => enginePower.value >= minEnginePower,
    );
}

// Seats
export function minSeats(body) {
    const maxSeats = body.range_filters.max_seats
        ? parseInt(body.range_filters.max_seats)
        : 8;
    return seats.filter((seat) => seat.value <= maxSeats);
}

export function maxSeats(body) {
    const minSeats = body.range_filters.min_seats
        ? parseInt(body.range_filters.min_seats)
        : 2;
    return seats.filter((seat) => seat.value >= minSeats);
}
