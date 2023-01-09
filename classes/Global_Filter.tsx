import Filter from "./Filter";

// Global Filter
export default class Global_Filter {
  global_operation: string // and
  filter: Array<Filter>

  constructor(global_operation: string, filter: Array<Filter>) {
    this.global_operation = global_operation
    this.filter = filter
      }
}