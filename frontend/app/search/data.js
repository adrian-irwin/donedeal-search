export const years = Array.from(
    { length: new Date().getFullYear() - 1980 + 1 },
    (_, i) => String(i + 1980),
);

export const prices = [
    ...Array.from({ length: 71 }, (_, i) => String(i * 500)),
    ...Array.from({ length: 7 }, (_, i) => String((i + 4) * 10000)),
].map((price) => {
    return {
        label: `€${price.replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`,
        value: price,
    };
});

export const mileages = [
    ...["0", "1000"],
    ...Array.from({ length: 20 }, (_, i) => String((i + 1) * 5000)),
    ...Array.from({ length: 10 }, (_, i) => String((i + 1) * 20000 + 100000)),
    ...["350000", "400000", "450000", "500000"],
].map((mileage) => {
    return {
        label: `${mileage.replace(/\B(?=(\d{3})+(?!\d))/g, ",")} km`,
        value: mileage,
    };
});

export const engineSizes = [
    ...Array.from({ length: 11 }, (_, i) => String(i * 100 + 1000)),
    ...["2500", "3000", "4000", "5000"],
].map((engineSize) => {
    return {
        label: `${engineSize.charAt(0)}.${engineSize.charAt(1)}L`,
        value: engineSize,
    };
});

export const enginePowers = Array.from({ length: 10 }, (_, i) =>
    String((i + 1) * 50),
).map((enginePower) => {
    return {
        label: `${enginePower} hp`,
        value: enginePower,
    };
});

export const seats = Array.from({ length: 7 }, (_, i) => String(i + 2)).map(
    (seat) => {
        return {
            label: `${seat} seats`,
            value: seat,
        };
    },
);
