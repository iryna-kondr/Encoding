import Title from "./Title"
import Visualization from "./Visualization"
import Global_Filter from "./Global_Filter"

// Dashboard 
export default class Dashboard {
  title: Title // New Hires
  purpose: string // Allow in-depth investigation of New Hires statistics
  task: string // Show New Hires statistics
  layout: string // ?
  visualization: Array<Visualization>
  global_filter: Global_Filter

  constructor(title: Title, purpose: string, task: string, layout: string, visualization: Array<Visualization>, global_filter: Global_Filter) {
    this.title = title
    this.purpose = purpose
    this.task = task
    this.layout = layout
    this.visualization = visualization
    this.global_filter = global_filter
  }
  }