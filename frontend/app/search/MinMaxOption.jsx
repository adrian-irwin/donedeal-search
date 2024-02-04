import { Select } from "@mantine/core";

export default function MinMaxOption({
    body,
    setBody,
    minSetValue,
    maxSetValue,
    minData,
    maxData,
    minPlaceholder,
    maxPlaceholder,
    minValue,
    maxValue,
}) {
    return (
        <div className="grid grid-cols-2 gap-0 pt-3">
            <Select
                data={minData}
                placeholder={minPlaceholder}
                value={minValue}
                onChange={(value) => {
                    setBody({
                        ...body,
                        range_filters: {
                            ...body.range_filters,
                            [minSetValue]: value,
                        },
                    });
                }}
                radius={0}
                searchable
                clearable
                allowDeselect
                nothingFoundMessage="Nothing found..."
                onClear={() => {
                    setBody({
                        ...body,
                        range_filters: {
                            ...body.range_filters,
                            [minSetValue]: undefined,
                        },
                    });
                }}
            />
            <Select
                data={maxData}
                placeholder={maxPlaceholder}
                value={maxValue}
                onChange={(value) => {
                    setBody({
                        ...body,
                        range_filters: {
                            ...body.range_filters,
                            [maxSetValue]: value,
                        },
                    });
                }}
                radius={0}
                searchable
                clearable
                allowDeselect
                nothingFoundMessage="Nothing found..."
                onClear={() => {
                    setBody({
                        ...body,
                        range_filters: {
                            ...body.range_filters,
                            [maxSetValue]: undefined,
                        },
                    });
                }}
            />
        </div>
    );
}
