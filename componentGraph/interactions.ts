import Effect from "./effect";

class Interactions {
    description: string;
    effectTypes: InteractionType[];
    effects: Effect[];
  
    constructor() {
      this.description = "";
      this.effectTypes = [];
      this.effects = [];
    }

    setInteractionData(){
        this.description = this.getDescriptionData();
        this.effectTypes = this.getEffectTypesData();
        this.effects = this.getEffectsData();
    }

    getDescriptionData(){
        return "";
    }

    getEffectTypesData(){
        return [];
    }

    getEffectsData(){
        return [];
    }
  }

  export enum InteractionType
{
    FILTERING = "filtering",
    HIGHLIGHTING = "highlighting",
}
  
  export default Interactions;