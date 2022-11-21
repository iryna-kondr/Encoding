# CARD 1
{   # Type of the visualization
    "type": "Card",
    # Task (WHY?) Provide a comprehensive view of everything p.55 (Tamara M.)
    "task": "summarize",
    # Description of the chart
    "description": "The card shows the number of new hires",
    "title": {  # Title for the chart
        "text": "New Hires"
    },
    # All attributes used in a visualization and their types
    "data": {"attribute": "New Hires", "type": "quantitative"},
    # Global filter (applied to all visualizations)
    "global_filter": {"and":
                      [{"attribute": "Year", "equal": 2014},
                       {"not": {"attribute": "Month", "equal": "Dec"}}
                       ]},
    "aggregate": {  # Array of objects that define attributes to aggregate
        "op": "sum",  # The aggregation operation to apply to the attributes
        # The data attribute for which to compute aggregate function
        "attribute": "New Hires",
        # The output attribute names to use for each aggregated attribute
        "as": "New Hires"
    },
    "mark": "card",  # A string describing the mark type (no such a mark according to Tamara M.)
    "insight": ""
}
# CARD 2
{
    "type": "Card",
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
    "type": "Filter",
    "task": "discover, derive, explore",
    # Find a new knowledge that was not previously known;
    # Produce new data elements based on exising data elements;
    # Searching for characteristics without regard to their location, often beginning from an overview of everything
    "description": "The filter allows filtering by Region.",
    "title": {
        "text": "Region"
    },
    "data": {"attribute": "Region", "type": "categorical"},
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
    "mark": "filter",
    "insight": ""
}
# FILTER 2
{
    "type": "Filter",
    "task": "discover, derive, explore",
    "description": "The filter allows filtering by Ethnicity.",
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
         "filtering": {"interaction_attribute": "Ethnicity",
                       "interaction_chart": ["New Hires", "New Hires SPLY",
                                             "New Hires and Hew Hires Same Period Last Year", "New Hires by Month and FPDesc",
                                             "New Hires by Region and Ethnicity"]}}
    ],
    "mark": "filter",
    "insight": ""
}
# LINE CHART
{
    "type": "Line chart",
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
        "legend": {"attribute": "FPDesc", "type": "categorical"}
    },
    "insight": ""
}
# CLUSTERED BAR CHART
{
    "type": "Clustered bar chart",
    "task": "part-to-whole relationship, lookup values, find trends",  # p. 153
    "description": "The clustered bar chart displayes the New Hires.",
    "title": {
        "text": "New Hires by Region and Ethnicity"
    },
    "data": [{"attribute": "New Hires", "type": "quantitative"},
             {"attribute": "Region", "type": "categorical"},
             {"attribute": "VP", "type": "categorical"},
             {"attribute": "Ethnicity", "type": "categorical"}],
    "global_filter": {"and":
                      [{"attribute": "Year", "equal": 2014},
                       {"not": {"attribute": "Month", "equal": "Dec"}}
                       ]},
    "interactions": [
        {"description": "",
         "highlighting": {"interaction_attribute": "Region",
                       "interaction_chart": ["New Hires and Hew Hires Same Period Last Year", "New Hires by Region and Ethnicity"]},
         "filtering": {"interaction_attribute": "Region",
                       "interaction_chart": ["New Hires", "New Hires SPLY", "New Hires by Month and FPDesc"]}},
        {"description": "",
         "highlighting": {"interaction_attribute": "Ethnicity",
                       "interaction_chart": ["New Hires and Hew Hires Same Period Last Year", "New Hires by Region and Ethnicity"]},
         "filtering": {"interaction_attribute": "Ethnicity",
                       "interaction_chart": ["New Hires", "New Hires SPLY", "New Hires by Month and FPDesc"]}}
    ],
    "mark": "line", # p.97 (Tamara M.)
    "visual_channel": "position, color",
    "encoding": {
        "x_axis": {"aggregate": "sum", "attribute": "New Hires", "type": "quantitative", "title": None},
        "y_axis": [{"attribute": "Region", "type": "categorical", "title": None},
                   {"attribute": "VP", "type": "categorical", "title": None}],
        "legend": {"attribute": "Ethnicity", "type": "categorical"}
    },
    "insight": ""
}
# LINE CLUSTERED COLUMN COMBO CHART
{
    "type": "Line clustered column combo chart",
    "task": "compare, lookup values, find trends",
    "description": "This element is a line clustered column combo chart.",
    "title": {
        "text": "New Hires and New Hires Same Period Last Year"
    },
    "data": [{"attribute": "New Hires", "type": "quantitative"},
             {"attribute": "New Hires SPLY", "type": "quantitative"},
             {"attribute": "Month", "type": "temporal"}],
    "global_filter": {"and":
                      [{"attribute": "Year", "equal": 2014},
                       {"not": {"attribute": "Month", "equal": "Dec"}}
                       ]},
    "interactions": [
        {"description": "",
         "highlighting": {"interaction_attribute": "Month",
                       "interaction_chart": ["New Hires and Hew Hires Same Period Last Year", "New Hires by Region and Ethnicity"]},
         "filtering": {"interaction_attribute": "Month",
                       "interaction_chart": ["New Hires", "New Hires SPLY", "New Hires by Month and FPDesc"]}},
        {"description": "",
         "highlighting": {"interaction_attribute": ["New Hires", "New Hires SPLY"],
                       "interaction_chart": ["New Hires and Hew Hires Same Period Last Year"]}}
    ],
    "layer": [
        {
            "mark": "line", # bar chart
            "encoding": {
                "x_axis": {"attribute": "Month", "type": "temporal", "title": None},
                "y_axis": [{"aggregate": "sum", "attribute": "New Hires", "type": "quantitative", "title": None},
                           {"aggregate": "sum", "attribute": "New Hires SPLY", "type": "quantitative", "title": None}]
            }
        },
        {
            "mark": "line", # line chart
            "encoding": {
                "x": None,
                "y": None,
                "legend": None
            }
        }
    ],
    "visual_channel": "position, color",
    "insight": ""
}
