# CARD 1
{
    # Provide a comprehensive view of everything p.55 (Tamara M.)
    "task": "summarize",
    # Description of the mark for commenting purpose.
    "description": "The card shows the number of new hires",
    "title": {  # Title for the plot.
        "text": "New Hires"
    },
    # All attributes used in a visualization and their types
    "data": {"attribute": "New Hires", "type": "quantitative"},
    "global_filter": {"and":
                      [{"attribute": "Year", "equal": 2014},
                       {"not": {"attribute": "Month", "equal": "Dec"}}
                       ]},
    "aggregate": {  # Array of objects that define attributes to aggregate.
        "op": "sum",  # The aggregation operation to apply to the attributes
        # The data attribute for which to compute aggregate function.
        "attribute": "New Hires",
        # The output attribute names to use for each aggregated attribute.
        "as": "New Hires"
    },
    "mark": "card",  # A string describing the mark type
    "insight": ""
}
# CARD 2
{
    "task": "summarize",
    "description": "The card shows the number of new hires same period last year",
    "title": {
        "text": "New Hires SPLY"
    },
    "data": {"attribute": "New Hires SPLY", "type": "quantitative"},
    "global_filter": {"and":
                      [{"attribute": "Year", "equal": 2014},
                       {"not": {"attribute": "Month", "equal": "Dec"}}
                       ]},
    "aggregate": {
        "op": "sum",
        "attribute": "New Hires SPLY",
        "as": "New Hires SPLY"
    },
    "mark": "card",
    "insight": ""
}
# FILTER 1
{
    "task": "discover, derive, explore",
    # Find a new knowledge that was not previously known;
    # Produce new data elements based on exising data elements;
    # Searching for characteristics without regard to their location, often beginning from an overview of everything
    "description": "The slicer allows filtering by Region.",
    "title": {
        "text": "Region"
    },
    "data": {"attribute": "Region", "type": "categorical"},
    "global_filter": {"and":
                      [{"attribute": "Year", "equal": 2014},
                       {"not": {"attribute": "Month", "equal": "Dec"}}
                       ]},
    # "interaction": {
    #     "filtering": {
    #         "interaction_attribute": ["Region"],
    #         "interaction_chart": ["New Hires", "New Hires SPLY",
    #                               "New Hires and Hew Hires Same Period Last Year", "New Hires by Month and FPDesc",
    #                               "New Hires by Region and Ethnicity"]}
    # },
    "interactions": [
        {"description": "",
         "filtering": {"interaction_attribute": "Region",
                       "interaction_chart": ["New Hires", "New Hires SPLY",
                                             "New Hires and Hew Hires Same Period Last Year", "New Hires by Month and FPDesc",
                                             "New Hires by Region and Ethnicity"]}}
    ],
    "mark": "slicer",
    "insight": ""
}
# FILTER 2
{
    "task": "discover, derive, explore",
    "description": "The slicer allows filtering by Ethnicity.",
    "title": {
        "text": "Ethnicity"
    },
    "data": {"attribute": "Ethnicity", "type": "categorical"},
    "global_filter": {"and":
                      [{"attribute": "Year", "equal": 2014},
                       {"not": {"attribute": "Month", "equal": "Dec"}}
                       ]},
    "interactions": [
        {"description": "",
         "filtering": {"interaction_attribute": "Region",
                       "interaction_chart": ["New Hires", "New Hires SPLY",
                                             "New Hires and Hew Hires Same Period Last Year", "New Hires by Month and FPDesc",
                                             "New Hires by Region and Ethnicity"]}}
    ],
    "mark": "slicer",
    "insight": ""
}
# LINE CHART
{
    "task": "show trend",  # p. 156
    "description": "The line chart shows the development of the New Hires over the Month.",
    "title": {
        "text": "New Hires by Month and FPDesc"
    },
    "data": [{"attribute": "New Hires", "type": "quantitative"},
             {"attribute": "Month", "type": "temporal"}],
    "global_filter": {"and":
                      [{"attribute": "Year", "equal": 2014},
                       {"not": {"attribute": "Month", "equal": "Dec"}}
                       ]},
    "interactions": [
        {"description": "",
         "highlighting": {"interaction_attribute": "Month",
                       "interaction_chart": ["New Hires and Hew Hires Same Period Last Year", "New Hires by Month and FPDesc", "New Hires by Region and Ethnicity"]},
         "filtering": {"interaction_attribute": "Month",
                       "interaction_chart": ["New Hires", "New Hires SPLY"]}},
        {"description": "",
         "highlighting": {"interaction_attribute": "Month, FPDesc",
                       "interaction_chart": ["New Hires and Hew Hires Same Period Last Year", "New Hires by Month and FPDesc", "New Hires by Region and Ethnicity"]},
         "filtering": {"interaction_attribute": "Month, FPDesc",
                       "interaction_chart": ["New Hires", "New Hires SPLY"]}}
    ],
    "mark": "line",
    "visual_channel": "position, color",
    "encoding": {
        "x_axis": {"attribute": "Month", "type": "temporal", "title": None},
        "y_axis": {"aggregate": "sum", "attribute": "New Hires", "type": "quantitative", "title": None},
        "legend": {"attribute": "FPDesc", "type": "nominal"}
    },
    "insight": ""
}
# CLUSTERED BAR CHART
{
    "task": "part-to-whole relationship, lookup values, find trends",  # p. 153
    "description": "The clustered bar chart displayes the New Hires.",
    "title": {
        "text": "New Hires by Region and Ethnicity"
    },
    "data": {""},
    "transform": [
        {"filter": {"and":
                    [{"attribute": "Year", "equal": 2014},
                     {"not": {"attribute": "Month", "equal": "Dec"}},
                     # MORE FILTERS CAN BE ADDED
                     ]}},
        {"highlighter": {"and":
                         [{"attribute": "Ethnicity", "equal": ""},
                          {"attribute": "Region", "equal": ""}
                          ]}}
    ],
    "mark": "bar",
    "encoding": {
        "x": {"aggregate": "sum", "attribute": "New Hires", "type": "quantitative", "title": None},
        "y": {"attribute": "Region", "type": "nominal", "title": None},
        "y2": {"attribute": "VP", "type": "nominal", "title": None},
        "legend": {"attribute": "Ethnicity", "type": "nominal"}
    }
}
# LINE CLUSTERED COLUMN COMBO CHART
{
    "task": "compare, lookup values, find trends",
    "description": "This element is a line clustered column combo chart.",
    "title": {
        "text": "New Hires and New Hires Same Period Last Year"
    },
    "data": {""},
    "transform": [
        {"filter": {"and":
                    [{"attribute": "Year", "equal": 2014},
                     {"not": {"attribute": "Month", "equal": "Dec"}},
                     # MORE FILTERS CAN BE ADDED
                     ]}},
        {"highlighter": {"attribute": "Month", "equal": ""}}
    ],
    "layer": [
        {
            "mark": "bar",
            "encoding": {
                "x": {"attribute": "Month", "type": "temporal", "title": None},
                "y": {"aggregate": "sum", "attribute": "New Hires", "type": "quantitative", "title": None},
                "y2": {"aggregate": "sum", "attribute": "New Hires SPLY", "type": "quantitative", "title": None}
            }

        },
        {
            "mark": "line",
            "encoding": {
                "x": None,
                "y": None,
                "legend": None
            }
        }
    ]


}
