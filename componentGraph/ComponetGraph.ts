import Dashboard from './Dashboard';

class ComponentGraph {
    dashboard: Dashboard;
  
    constructor() {
      this.dashboard = new Dashboard();
    }

    setComponentGraphData(){
       this.dashboard.setDashboardData();
       localStorage.setItem("componentGraph", JSON.stringify(this.dashboard));
    }

    getComponentGraph(){
      //print it to the console for now we can safe it to a veriable later on when we need it
      console.log(JSON.parse(localStorage.getItem("componentGraph")!));
  }

  }

  //how to create component graph and test if it is correct:
  //let graph = new ComponentGraph();
  //graph.setComponentGraphData();
  //graph.getComponentGraph();

export default ComponentGraph;