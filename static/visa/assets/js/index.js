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
	

  



   // chart 6
    // var ctx = document.getElementById("chart6").getContext('2d');
   
    //   var gradientStroke3 = ctx.createLinearGradient(0, 0, 0, 300);
    //   gradientStroke3.addColorStop(0, '#42e695');
    //   gradientStroke3.addColorStop(1, '#3bb2b8');

    //   var gradientStroke4 = ctx.createLinearGradient(0, 0, 0, 300);
    //   gradientStroke4.addColorStop(0, '#42e695');
    //   gradientStroke4.addColorStop(0.25, '#3bb2b8');

    //   var myChart = new Chart(ctx, {
    //     type: 'horizontalBar',
    //     data: {
    //       labels: ['Documents added', 'Sent for visa processing', 'Visa approved', 'Application rejected',],
    //       datasets: [{
    //         label: 'Visa applications',
    //         data: [40, 30, 61, 35, ],
    //         borderColor: gradientStroke3,
    //         backgroundColor: gradientStroke3,
    //         hoverBackgroundColor: gradientStroke4,
    //         hoverBorderColor: gradientStroke4,
    //         pointRadius: 0,
    //         fill: false,
    //         borderWidth: 1
    //       },]
    //     },
    //     options:{
    //       maintainAspectRatio: false,
    //       legend: {
    //         position: 'bottom',
    //         display: true,
    //         labels: {
    //           boxWidth:25
    //         }
    //       },
    //       title: {
    //         display: true,
    //         text: 'VISA APPLICATION STATUS'
    //       },
    //       tooltips: {
    //         displayColors:false,
    //       },	
    //       scales: {
    //         xAxes: [{
    //           ticks: {
    //             beginAtZero: true
    //           }
    //         }],
    //         yAxes: [{
    //           barPercentage: .7,
    //         }],
    //       }
    //     }
    //   });
	  
	  
	  
	  
  // chart 7
//  var ctx = document.getElementById('chart7').getContext('2d');

//   var gradientStroke1 = ctx.createLinearGradient(0, 0, 0, 300);
//       gradientStroke1.addColorStop(0, '#ee0979');
//       gradientStroke1.addColorStop(1, '#ff6a00');

//       var myChart = new Chart(ctx, {
//         type: 'line',
//         data: {
//           labels: [1, 2, 3, 4, 5, 6, 7],
//           datasets: [{
//             label: 'Views',
//             data: [3, 30, 10, 10, 22, 12, 5],
//             pointBorderWidth: 2,
//             pointHoverBackgroundColor: gradientStroke1,
//             backgroundColor: gradientStroke1,
//             borderColor: 'transparent',
//             borderWidth: 1
//           }]
//         },
//         options: {
//           maintainAspectRatio: false,
//             legend: {
// 			  position: 'bottom',
//               display:false
//             },
//             tooltips: {
// 			  displayColors:false,	
//               mode: 'nearest',
//               intersect: false,
//               position: 'nearest',
//               xPadding: 10,
//               yPadding: 10,
//               caretPadding: 10
//             },
// 			scales: {
// 			  xAxes: [{
// 				ticks: {
//                     beginAtZero:true
//                 },
// 				gridLines: {
// 				  display: true 
// 				},
// 			  }],
// 			   yAxes: [{
// 				ticks: {
//                     beginAtZero:true
//                 },
// 				gridLines: {
// 				  display: true 
// 				},
// 			  }]
// 		     }

//          }
//       });  
	  
	  
	  

// world map

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
	

  // chart 16
  var ctx = document.getElementById("chart16").getContext('2d');

    var gradientStroke5 = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStroke5.addColorStop(0, '#7f00ff');
      gradientStroke5.addColorStop(1, '#e100ff');

      var gradientStroke6 = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStroke6.addColorStop(0, '#fc4a1a');
      gradientStroke6.addColorStop(1, '#f7b733');


      var gradientStroke7 = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStroke7.addColorStop(0, '#283c86');
      gradientStroke7.addColorStop(1, '#45a247');

      var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ["Samsung", "Apple", "Nokia"],
          datasets: [{
            backgroundColor: [
              gradientStroke5,
              gradientStroke6,
              gradientStroke7
            ],

             hoverBackgroundColor: [
              gradientStroke5,
              gradientStroke6,
              gradientStroke7
            ],

            data: [50, 50, 50]
          }]
        },
        options: {
          maintainAspectRatio: false,
            legend: {
              display: false
            },
            tooltips: {
			  displayColors:false
            }
        }
      });


	  
// chart 17
var ctx = document.getElementById("chart17").getContext('2d');

  var gradientStroke8 = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStroke8.addColorStop(0, '#42e695');
      gradientStroke8.addColorStop(1, '#3bb2b8');

      var gradientStroke9 = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStroke9.addColorStop(0, '#4776e6');
      gradientStroke9.addColorStop(1, '#8e54e9');


      var gradientStroke10 = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStroke10.addColorStop(0, '#ee0979');
      gradientStroke10.addColorStop(1, '#ff6a00');

      var myChart = new Chart(ctx, {
        type: 'polarArea',
        data: {
          labels: ["Gross Profit", "Revenue", "Expense"],
          datasets: [{
            backgroundColor: [
              gradientStroke8,
              gradientStroke9,
              gradientStroke10
            ],

             hoverBackgroundColor: [
              gradientStroke8,
              gradientStroke9,
              gradientStroke10
            ],
            data: [5, 8, 7]
          }]
        },
        options: {
          maintainAspectRatio: false,
            legend: {
              display: false
            },
            tooltips: {
			  displayColors:false
            }
        }
      });


// chart 18
var ctx = document.getElementById("chart18").getContext('2d');

    var gradientStroke11 = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStroke11.addColorStop(0, '#ba8b02');
      gradientStroke11.addColorStop(1, '#181818');

      var gradientStroke12 = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStroke12.addColorStop(0, '#2c3e50');
      gradientStroke12.addColorStop(1, '#fd746c');


      var gradientStroke13 = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStroke13.addColorStop(0, '#ff0099');
      gradientStroke13.addColorStop(1, '#493240');

      var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ["Jeans", "T-Shirts", "Shoes"],
          datasets: [{
            backgroundColor: [
              gradientStroke11,
              gradientStroke12,
              gradientStroke13
            ],
            hoverBackgroundColor: [
              gradientStroke11,
              gradientStroke12,
              gradientStroke13
            ],
            data: [25, 25, 25]
          }]
        },
        options: {
          maintainAspectRatio: false,
            legend: {
              display: false
            },
            tooltips: {
			  displayColors:false
            }
        }
      });
	  
	  
	  
});

