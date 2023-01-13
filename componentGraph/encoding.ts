import Legend from "./legend";
import Value from "./value";
import XAxis from "./xAxis";
import YAxis from "./yAxis";

class Encoding {
    xAxis: XAxis;
    yAxis: YAxis;
    legend: Legend;
    value: Value;
  
    constructor() {
      this.xAxis = new XAxis();
      this.yAxis = new YAxis();
      this.legend = new Legend();
      this.value = new Value();
    }

    setEncodingData(){
        this.xAxis.setXAxisData();
        this.yAxis.setYAxisData();
        this.legend.setLegendData();
        this.value.setValueData();
    }
  }
  
  export default Encoding;