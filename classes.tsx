// Insight
class Insight {
  text: string; // The peak of new hires was in September
  attribute: string; // New Hires 
}

// Title
class Title {
  text: string; // New Hires and New Hires Same Period Last Year
}

// Data
class Data {
  attribute: string; // eg New Hires
  type: string; // eg quantitative
}

// Visual Channel
class Visual_Channel {
  channel: string; // position, color
}

// Filter
class Filter {
  attribute: string; // Year
  value: string | number; // 2014
  operation: string; // equal
}

// Global Filters
class Global_Filters {
  global_operation: string; // and
  filters: Array<Filter>; 
}

// Visualization
class Visualization {
  type: string; // Line Clustered Column Combo Chart
  task: string; // Lookup and compare values 
  description: string; // The chart shows New Hires and New Hires SPLY for specific time periods
  mark: string; // line
  data: Array<Data>;
  insight: Insight;
  title: Title;
  visual_channel: Visual_Channel;
  global_filter: Array<Global_Filters>
}

// Dashboard 
class Dashboard {
  title: Title; // New Hires
  purpose: string; // Allow in-depth investigation of New Hires statistics
  task: string; // Show New Hires statistics
  layout: string; // ?
  visualization: Array<Visualization>;
  global_filters: Array<Global_Filters>
}

