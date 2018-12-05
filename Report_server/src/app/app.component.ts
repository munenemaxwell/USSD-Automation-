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

  
  constructor(
    private status :PassService,
    //private canvas :CanvasJS


  ) { }

  display(data){

    let dataPoints = [
      {y: 79.45, label: "Passed"},
			{y: 7.31, label: "Failed"},
			{y: 7.06, label: "Unknown"}
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