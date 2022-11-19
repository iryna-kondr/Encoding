# CARD 1
{
    "description": "The card shows the number of new hires", # Description of the mark for commenting purpose.
    "title": {  # Title for the plot.
        "text": "New Hires"
    },
    "data": {""},     # An object describing the data source. Set to null to ignore the parent’s data source. If no data is set, it is derived from the parent.
    "transform": [  # An array of data transformations such as filter and new field calculation.
        {"filter": {"and":
                    [{"field": "Year", "equal": 2014},
                     {"not": {"field": "Month", "equal": "Dec"}},
                     # MORE FILTERS CAN BE ADDED
                     ]}},
        {
            "aggregate": [{  # Array of objects that define fields to aggregate.
                "op": "sum",  # The aggregation operation to apply to the fields
                "field": "New Hires", # The data field for which to compute aggregate function.
                "as": "New Hires" # The output field names to use for each aggregated field.
            }]
        }
    ],
    "mark": "card"  # A string describing the mark type
}
# CARD 2
{
    "description": "The card shows the number of new hires same period last year",
    "title": {
        "text": "New Hires SPLY"
    },
    "data": {""},
    "transform": [
        {"filter": {"and":
                    [{"field": "Year", "equal": 2014},
                     {"not": {"field": "Month", "equal": "Dec"}},
                     # MORE FILTERS CAN BE ADDED
                     ]}},
        {
            "aggregate": [{
                "op": "sum",
                "field": "New Hires SPLY",
                "as": "New Hires SPLY"
            }]
        }
    ],
    "mark": "card"
}
# FILTER 1
{
    "description": "The slicer allows filtering by Region.",
    "title": {
        "text": "Region"
    },
    "data": {""},
    "transform": [
        {"filter": {"field": "Region", "oneOf": ["", ""]}}
    ],
    "mark": "slicer"
}
# FILTER 2
{
    "description": "The slicer allows filtering by Ethnicity.",
    "title": {
        "text": "Ethnicity"
    },
    "data": {""},
    "transform": [
        {"filter": {"field": "Ethnicity", "oneOf": ["", ""]}}
    ],
    "mark": "slicer"
}
# LINE CHART
{
    "description": "The line chart shows the development of the New Hires over the Month.",
    "title": {
        "text": "New Hires by Month and FPDesc"
    },
    "data": {""},
    "transform": [
        {"filter": {"and":
                    [{"field": "Year", "equal": 2014},
                     {"not": {"field": "Month", "equal": "Dec"}},
                     # MORE FILTERS CAN BE ADDED
                     ]}},
        {"highlighter": {"field": "Month", "equal": ""}}
    ],
    "mark": "line",
    "encoding": {
        "x": {"field": "Month", "type": "temporal", "title": None},
        "y": {"aggregate": "sum", "field": "New Hires", "type": "quantitative", "title": None},
        "color": {"field": "FPDesc", "type": "nominal"}
    }
}
# CLUSTERED BAR CHART
{
    "description": "The clustered bar chart displayes the New Hires.",
    "title": {
        "text": "New Hires by Region and Ethnicity"
    },
    "data": {""},
    "transform": [
        {"filter": {"and":
                    [{"field": "Year", "equal": 2014},
                     {"not": {"field": "Month", "equal": "Dec"}},
                     # MORE FILTERS CAN BE ADDED
                     ]}},
        {"highlighter": {"and":
                         [{"field": "Ethnicity", "equal": ""},
                          {"field": "Region", "equal": ""}
                          ]}}
    ],
    "mark": "bar",
    "encoding": {
        "x": {"aggregate": "sum", "field": "New Hires", "type": "quantitative", "title": None},
        "y": {"field": "Region", "type": "nominal", "title": None},
        "y2": {"field": "VP", "type": "nominal", "title": None},
        "color": {"field": "Ethnicity", "type": "nominal"}
    }
}
# LINE CLUSTERED COLUMN COMBO CHART
{
    "description": "This element is a line clustered column combo chart.",
    "title": {
        "text": "New Hires and New Hires Same Period Last Year"
    },
    "data": {""},
    "transform": [
        {"filter": {"and":
                    [{"field": "Year", "equal": 2014},
                     {"not": {"field": "Month", "equal": "Dec"}},
                     # MORE FILTERS CAN BE ADDED
                     ]}},
        {"highlighter": {"field": "Month", "equal": ""}}
    ],
    "layer": [
        {
            "mark": "bar",
            "encoding": {
                "x": {"field": "Month", "type": "temporal", "title": None},
                "y": {"aggregate": "sum", "field": "New Hires", "type": "quantitative", "title": None},
                "y2": {"aggregate": "sum", "field": "New Hires SPLY", "type": "quantitative", "title": None}
            }

        },
        {
            "mark": "line",
            "encoding": {
                "x": None,
                "y": None,
                "color": None
            }
        }
    ]


}
