import Data from "./Data"
import Insight from "./Insight"
import Title from "./Title"
import Visual_Channel from "./Visual_Channel"
import Global_Filter from "./Global_Filter"
import Interactions from "./interactions"
import Encoding from "./encoding"

// Visualization
export default class Visualization {
  type: string // Line Clustered Column Combo Chart
  task: string // Lookup and compare values 
  description: string // The chart shows New Hires and New Hires SPLY for specific time periods
  mark: Array<string> // line
  data: Array<Data>
  insight: Insight
  title: Title
  visual_channel: Array<Visual_Channel>
  global_filter: Global_Filter
  interactions: Interactions[]
  encoding: Encoding[]

  constructor(type: string, task: string, description: string, mark: Array<string>, data: Array<Data>, insight: Insight, title: Title, visual_channel: Array<Visual_Channel>, global_filter: Global_Filter) {
    this.type = type
    this.task = task
    this.description = description
    this.mark = mark
    this.data = data
    this.insight = insight
    this.title = title,
    this.visual_channel = visual_channel,
    this.global_filter = global_filter
    this.interactions = []
    this.encoding = []
  }
}