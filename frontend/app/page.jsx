"use client";

import FullSearch from "@/app/search/FullSearch";
import { useState } from "react";

export default function Home() {
    const [searchQuery, setSearchQuery] = useState([]);
    const [ads, setAds] = useState([]);

    const search = async () => {
        const response = await fetch(`http://localhost:5000/search`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ searchQuery }),
        });
        const data = await response.json();
        setAds(data);
    };

    return (
        <main className="flex min-h-screen flex-col items-center justify-between p-24">
            <div className="flex flex-col items-center justify-center">
                <h1 className="text-4xl font-bold mb-4">
                    Better DoneDeal Frontend
                </h1>

                <FullSearch />

                <button
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg mt-4"
                    onClick={() => {
                        console.log("clicked");
                    }}
                >
                    Search
                </button>
            </div>
            <div className="flex flex-col items-center justify-center">
                {ads.map((ad) => (
                    <div
                        key={ad.id}
                        className="flex flex-col items-center justify-center border border-gray-300 rounded-lg px-4 py-2 mt-4"
                    >
                        <Image
                            src={ad.image}
                            alt={ad.title}
                            width={256}
                            height={256}
                        />
                        <h2 className="text-2xl font-bold">{ad.title}</h2>
                        <p className="text-xl">{ad.price}</p>
                        <p className="text-xl">{ad.location}</p>
                    </div>
                ))}
            </div>
        </main>
    );
}
