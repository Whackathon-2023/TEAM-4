anychart.onDocumentReady(function() {
  anychart.data.loadJsonFile('https://gist.githubusercontent.com/shacheeswadia/47b28a4d061e415555f01f5ce48e9ae3/raw/0f7592a8048872db7b77ccd2df8907e61952a806/shippingDataInverted.json',
  function (data) {

      // set the color theme
      anychart.theme('darkGlamour');

      // set the map chart
      var map = anychart.map();

      // set the global geodata
      map.geoData('anychart.maps.world');

      // set the chart title
      map.title( 'Shipping ports across the globe');

      // create a dataset from data
      var portsDataSet = anychart.data.set(data).mapAs();

      // helper function to create several series
      var createSeries = function (name, data, color) {

          // set the marker series
          var series = map.marker(data);

          // configure the series settings
          series
              .name(name)
              .fill(color)
              .stroke('none')
              .type('circle')
              .size(3)
              .labels(false)
              .selectionMode('none');

          series
              .legendItem()
              .iconType('circle')
              .iconFill(color);
      };

      // create 5 series, filtering the data by the outflows at each port
      createSeries(
          'Up to 100,000',
          portsDataSet.filter('outflows', filterFunction(0, 100000)),
          '#D1FAE9'
      );
      createSeries(
          '100,000 - 1,000,000',
          portsDataSet.filter('outflows', filterFunction(100000, 1000000)),
          '#9CE0E5'
      );
      createSeries(
          '1,000,000 - 5,000,000',
          portsDataSet.filter('outflows', filterFunction(1000000, 5000000)),
          '#00ACC3'
      );
      createSeries(
          '5,000,000 - 10,000,000',
          portsDataSet.filter('outflows', filterFunction(5000000, 10000000)),
          '#355CB1'
      );
      createSeries(
          'More than 10,000,000 outflows',
          portsDataSet.filter('outflows', filterFunction(10000000, 0)),
          '#002D79'
      );

      // enable and configure the map tooltip
      map
          .tooltip() 
          .useHtml(true)
          .padding([8, 13, 10, 13])
          .width(350)
          .fontSize(12)
          .fontColor('#e6e6e6')
          .titleFormat(function () {
              return this.getData('Name');
          })
          .format(function () {
              return (
                  '<span style="color: #bfbfbf">Country: </span>'+
                  this.getData('Country') +
                  '<br/>' +
                  '<span style="color: #bfbfbf">Outflows: </span>' +
                  this.getData('outflows').toFixed(0)
              );
          });

      // turn on the map legend
      map.legend(true);

      // add zoom ui controls
      var zoomController = anychart.ui.zoom();
      zoomController.render(map);

      // set the container
      map.container('container');

      // draw the map
      map.draw();

  });
});

// helper filter function
function filterFunction(val1, val2) {
  if (val2) {
      return function (fieldVal) {
          return val1 <= fieldVal && fieldVal < val2;
      };
  }
  return function (fieldVal) {
      return val1 <= fieldVal;
  };
}
