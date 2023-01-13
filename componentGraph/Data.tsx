// Data
export default class Data {
  attribute: string // eg New Hires
  type: string // eg quantitative
  value: Array<number | string>

  constructor(attribute: string, type: string, value:  Array<number | string>) {
    this.attribute = attribute
    this.type = type
    this.value = value
  }
}