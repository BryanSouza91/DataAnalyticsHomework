// from data.js
var tableData = data;

// YOUR CODE HERE!

// Select the datetime input by user
var dateTime = d3.select("#datetime");


// Function to handle input change
function handleChange(event) {

  // Finally, add the summary stats to the `ul` tag
  var list = d3.select(".summary");

  list.html("");
  list.append("li").text(`Mean: ${mean}`);
  list.append("li").text(`Median: ${median}`);
  list.append("li").text(`Mode: ${mode}`);
  list.append("li").text(`Variance: ${variance}`);
  list.append("li").text(`Standard Deviation: ${stDev}`);
});