import Title from "./Title"
import Visualization from "./Visualization"
import Global_Filter from "./Global_Filter"
import * as global from "../onboarding/ts/globalVariables"

// Dashboard 
export default class Dashboard {
  title: Title // New Hires
  purpose: string // Allow in-depth investigation of New Hires statistics
  task: string // Show New Hires statistics
  layout: string // ?
  visualizations: Visualization[]
  global_filter: Global_Filter
  
  constructor() {
    this.title = new Title("");
    this.purpose = "";
    this.task = "";
    this.layout = "";
    this.visualizations = [];
    this.global_filter = new Global_Filter("", []);
  }

  setDashboardData(){
    this.title.setTitle();
    this.purpose = this.getPurposeData();
    this.task = this.getTaskData();
    this.layout = this.getLayoutData();
    this.visualizations = this.getVisualsData();
    this.global_filter.setGlobalFilter();
  }

  getPurposeData(){
    //ToDo get real value and combine it with predefined text and return it
    return "purpose";
  }

  getTaskData(){
    //ToDo get real value and combine it with predefined text and return it
    return "task";
  }

  getLayoutData(){
    let numberOfVisuals = global.allVisuals.length;
    let numberOfFilters = this.global_filter.filter.length;
    let defaultLayoutText = "This dashboard shows " + numberOfVisuals + " visuals and " + numberOfFilters + " global filters."
    return defaultLayoutText;
  }

  getVisualsData(){
    //ToDo create empty array
    //ToDo for loop over all visuals in this dashboard
      //ToDo call setVisualizationData(from Visualization class) to get all info in the right format
      //ToDo add to array
    return[] //ToDo return created array
  }
}