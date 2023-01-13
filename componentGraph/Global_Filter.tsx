import Filter from "./Filter";

// Global Filter
export default class Global_Filter {
  global_operation: string // and
  filter: Array<Filter>

  constructor(global_operation: string, filter: Array<Filter>) {
    this.global_operation = global_operation
    this.filter = filter
      }

  setGlobalFilter(){
    //ToDo get real operation and set variable to real value
    this.global_operation = "operation";
    this.filter = this.getFilterData();
  }

  getFilterData(){
    //ToDo get real data of all filters and return it as an array
    return [];
  }
}