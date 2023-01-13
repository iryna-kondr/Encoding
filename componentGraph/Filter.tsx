// Filter
export default class Filter {
  attribute: string // Year
  value: string | number // 2014
  operation: string // equal

  constructor(attribute: string, value: string | number, operation: string) {
    this.attribute = attribute
    this.value = value
    this.operation = operation
  }
}