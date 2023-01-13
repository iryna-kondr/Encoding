class Effect {
    interactionAttribute : string;
    interactionChart: string[];
  
    constructor() {
      this.interactionAttribute = "";
      this.interactionChart = [];
    }

    setEffectData(){
        this.interactionAttribute = this.getInteractionAttributeData();
        this.interactionChart = this.getInteractionChartData();
    }

    getInteractionAttributeData(){
        return "";
    }

    getInteractionChartData(){
        return [];
    }
  }
  
  export default Effect;