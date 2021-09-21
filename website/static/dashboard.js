function myFunc(vars) {

  var ctx = document.getElementById('myChart');

  obj = vars;
  // var obj = JSON.parse(vars);
      
  var labels = Object.keys(obj); //obj.keys;

  var data = Object.values(obj);
  // for (var x in obj) {
  //   data[data.length] = x;
  // }

  var config = {
     type: 'line',
     data: {
        labels: labels,
        datasets: [{
           data: data,
           lineTension: 0,
           backgroundColor: 'transparent',
           borderColor: '#007bff',
           borderWidth: 4,
           pointBackgroundColor: '#007bff'
        }]
     },
     options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  };

  var chart = new Chart(ctx, config);
}