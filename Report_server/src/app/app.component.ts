import { Component } from '@angular/core';
import { PassService } from './pass.service'
//import CanvasJS from './CanvasJS';
import * as CanvasJS from './canvasjs.min';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  public title = 'Report';
  public status_obj ;
  public chart;
  public data;
  public passed =0;
  public failed =0;  
  public percentage_passed=0;
  public percentage_failed=0;
  public percentage_unknown=0;

  constructor(
    private status :PassService,
    //private canvas :CanvasJS


  ) { }

  compute(item){
    
    if(item.no_passed == 1){
      this.passed+=1;
    }
  }

  display(data){

    this.data=data;
    let length=data.length;
    let new_data=data.map((item)=>this.compute(item))
     this.failed=length -this.passed;

    //console.log('passed is '+this.passed+' failed is '+failed)
    this.percentage_passed=(this.passed/length)*100;
    this.percentage_failed=(this.failed/length)*100;
    this.percentage_unknown=0;

    let dataPoints = [
      {y: this.percentage_passed, label: "Passed Rate %"},
			{y: this.percentage_failed, label: "Failure Rate in %"},
			{y: this.percentage_unknown, label: "No Run(Manual test Verification required)"}
		];
		
		let chart = new CanvasJS.Chart("chartContainer",{
			animationEnabled: true,
			title:{
				text: "USSD AUTOMATION FOR "+data[0].title
			},
			data: [{
				type: "pie",
        dataPoints : dataPoints
        




        
			}]
		});
		chart.render();

   /* let chart= this.canvas.Chart("chartContainer", {
      animationEnabled: true,
    
      title: {
        text: "USSD TEST AUTOMATION FOR COMBO BUNDLES SUMMARY REPORT"
      },
      data: [{
        type: "pie",
        startAngle: 240,
        yValueFormatString: "##0.00\"%\"",
        indexLabel: "{label} {y}",
        dataPoints: [
          {y: 79.45, label: "Passed"},
          {y: 7.31, label: "Failed"},
          {y: 7.06, label: "Unknown"}
          
        ]
      }]
    });
    chart.render();*/
    console.log(data)


  }

  ngOnInit() {
    this.status.get_status().subscribe(
      data => this.display(data), //this.status_obj(data),
      error => console.log(error)
    );
}



}