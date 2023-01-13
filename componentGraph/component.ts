class Component {
    aggregate: ComponentAggregate;
    attribute: string; 
    type: ComponentType;
    title: string;
  
    constructor() {
      this.aggregate = ComponentAggregate.EMPTY;
      this.attribute = ""; 
      this.type = ComponentType.EMPTY;
      this.title = "";
    }

    setComponentData(){
        this.aggregate = this.getComponentAggregateData();
        this.attribute = this.getComponentAttributeData(); 
        this.type = this.getComponentTypeData();
        this.title = this.getComponentTitleData();
    }

    getComponentAggregateData(){
        return ComponentAggregate.EMPTY;
    }

    getComponentAttributeData(){
        return "";
    }

    getComponentTypeData(){
        return ComponentType.EMPTY;
    }

    getComponentTitleData(){
        return "";
    }
  }

export enum ComponentAggregate
{
    EMPTY = "",
    SUM = "sum",
}

export enum ComponentType
{
    EMPTY = "",
    QUANTITATIVE = "quantitative",
    TEMPORAL = "temporal",
    CATEGORICAL = "categorical",
}

export default Component;