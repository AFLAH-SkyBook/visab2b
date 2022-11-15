$(function() {
    "use strict";
	
	// chart 1
	$('#chart1').sparkline([5,8,7,10,9,10,8,6,4,6,8,7,6,8], {
            type: 'bar',
            height: '35',
            barWidth: '3',
            resize: true,
            barSpacing: '3',
            barColor: '#fff'
        });

    
	// chart 2
    $("#chart2").sparkline([0,5,3,7,5,10,3,6,5,10], {
            type: 'line',
            width: '80',
            height: '40',
            lineWidth: '2',
            lineColor: '#fff',
            fillColor: 'transparent',
            spotColor: '#fff',
        })
		
		
	// chart 3
     $("#chart3").sparkline([2,3,4,5,4,3,2,3,4,5,6,5,4,3,4,5], {
        type: 'discrete',
        width: '75',
        height: '40',
        lineColor: '#fff',
        lineHeight: 22

     });	
		

	// chart 4	
	$("#chart4").sparkline([5,6,7,9,9,5,3,2,2,4,6,7], {
		type: 'line',
		width: '100',
		height: '25',
		lineWidth: '2',
		lineColor: '#ffffff',
		fillColor: 'transparent'
		
	});
	


  // // chart 6
  //   var ctx = document.getElementById("chart6").getContext('2d');

  //     var myChart = new Chart(ctx, {
  //       type: 'bar',
  //       data: {
  //         labels: [1, 2, 3, 4, 5, 6, 7, 8],
  //         datasets: [{
  //           label: 'Laptops',
  //           data: [40, 30, 60, 35, 60, 25, 50, 40],
  //           borderColor: '#15ca20',
  //           backgroundColor: '#15ca20',
  //           hoverBackgroundColor: '#15ca20',
  //           pointRadius: 0,
  //           fill: false,
  //           borderWidth: 1
  //         }, {
  //           label: 'Mobiles',
  //           data: [50, 60, 40, 70, 35, 75, 30, 20],
  //           borderColor: '#b81cff',
  //           backgroundColor: '#b81cff',
  //           hoverBackgroundColor: '#b81cff',
  //           pointRadius: 0,
  //           fill: false,
  //           borderWidth: 1
  //         }]
  //       },
	// 	options:{
  //     maintainAspectRatio: false,
	// 	  legend: {
	// 		  position: 'bottom',
  //             display: true,
	// 		  labels: {
  //               boxWidth:12
  //             }
  //           },
	// 		tooltips: {
	// 		  displayColors:false,
	// 		},	
	// 	  scales: {
	// 		  xAxes: [{
	// 			barPercentage: .5
	// 		  }]
	// 	     }
	// 	}
  //     });
	  
	  
	  
	  
// chart 7
 var ctx = document.getElementById('chart7').getContext('2d');

      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: [1, 2, 3, 4, 5, 6, 7],
          datasets: [{
            label: 'Views',
            data: [3, 30, 10, 10, 22, 12, 5],
            pointBorderWidth: 2,
            pointHoverBackgroundColor: '#fd3550',
            backgroundColor: '#fd3550',
            borderColor: 'transparent',
            borderWidth: 1
          }]
        },
        options: {
          maintainAspectRatio: false,
            legend: {
			  position: 'bottom',
              display:false
            },
            tooltips: {
			  displayColors:false,	
              mode: 'nearest',
              intersect: false,
              position: 'nearest',
              xPadding: 10,
              yPadding: 10,
              caretPadding: 10
            },
			scales: {
			  xAxes: [{
				ticks: {
                    beginAtZero:true
                },
				gridLines: {
				  display: true 
				},
			  }],
			   yAxes: [{
				ticks: {
                    beginAtZero:true
                },
				gridLines: {
				  display: true 
				},
			  }]
		     }

         }
      });  
	  
	  
	  

// worl map

jQuery('#dashboard-map').vectorMap(
{
    map: 'world_mill_en',
    backgroundColor: 'transparent',
    borderColor: '#818181',
    borderOpacity: 0.25,
    borderWidth: 1,
    zoomOnScroll: false,
    color: '#009efb',
    regionStyle : {
        initial : {
          fill : '#15ca20'
        }
      },
    markerStyle: {
      initial: {
                    r: 9,
                    'fill': '#fff',
                    'fill-opacity':1,
                    'stroke': '#000',
                    'stroke-width' : 5,
                    'stroke-opacity': 0.4
                },
                },
    enableZoom: true,
    hoverColor: '#009efb',
    markers : [{
        latLng : [21.00, 78.00],
        name : 'I Love My India'
      
      }],
    hoverOpacity: null,
    normalizeFunction: 'linear',
    scaleColors: ['#b6d6ff', '#005ace'],
    selectedColor: '#c9dfaf',
    selectedRegions: [],
    showTooltip: true
});



  // chart 8
  $("#chart8").sparkline([3,5,3,7,5,10,3,6,5,0], {
    type: 'line',
    width: '150',
    height: '45',
    lineWidth: '2',
    lineColor: '#dd4b39',
    fillColor: 'rgba(221, 75, 57, 0.5)',
    spotColor: '#dd4b39',
}); 

// chart 9
$("#chart9").sparkline([3,5,3,7,5,10,3,6,5,0], {
    type: 'line',
    width: '150',
    height: '45',
    lineWidth: '2',
    lineColor: '#3b5998',
    fillColor: 'rgba(59, 89, 152, 0.5)',
    spotColor: '#3b5998',
});


// chart 10
$("#chart10").sparkline([3,5,3,7,5,10,3,6,5,0], {
    type: 'line',
    width: '150',
    height: '45',
    lineWidth: '2',
    lineColor: '#55acee',
    fillColor: 'rgba(85, 172, 238, 0.5)',
    spotColor: '#55acee',
});


// chart 11
$("#chart11").sparkline([3,5,3,7,5,10,3,6,5,0], {
    type: 'line',
    width: '150',
    height: '45',
    lineWidth: '2',
    lineColor: '#0976b4',
    fillColor: 'rgba(9, 118, 180, 0.5)',
    spotColor: '#0976b4',
});


// chart 12
$("#chart12").sparkline([3,5,3,7,5,10,3,6,5,0], {
    type: 'line',
    width: '150',
    height: '45',
    lineWidth: '2',
    lineColor: '#1769ff',
    fillColor: 'rgba(23, 105, 255, 0.5)',
    spotColor: '#1769ff',
});


// chart 13
$("#chart13").sparkline([3,5,3,7,5,10,3,6,5,0], {
    type: 'line',
    width: '150',
    height: '45',
    lineWidth: '2',
    lineColor: '#ea4c89',
    fillColor: 'rgba(234, 76, 137, 0.5)',
    spotColor: '#ea4c89',
});


// chart 14
$("#chart14").sparkline([3,5,3,7,5,10,3,6,5,0], {
    type: 'line',
    width: '150',
    height: '45',
    lineWidth: '2',
    lineColor: '#333333',
    fillColor: 'rgba(51, 51, 51, 0.5)',
    spotColor: '#333333',
});


// chart 15
$('#chart15').sparkline([5,8,7,10,9,10,8,6,4,6,8,7,6,8,10,8,6,0], {
    type: 'bar',
    width: '150',
    height: '45',
    barWidth: '3',
    resize: true,
    barSpacing: '5',
    barColor: '#fff'
});	
	  
});
