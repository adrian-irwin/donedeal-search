"use client";

import { SearchDataContext } from "@/app/contexts/SearchDataContext";
import RangeSearches from "@/app/search/RangeSearches";
import { useContext } from "react";

export default function FullSearch() {
    const { body, setBody } = useContext(SearchDataContext);
    return (
        <div className="flex flex-col items-center justify-center text-center">
            <h1>Full Search</h1>
            <div className="flex flex-row items-center justify-center">
                <RangeSearches body={body} setBody={setBody} />
            </div>
        </div>
    );
}
