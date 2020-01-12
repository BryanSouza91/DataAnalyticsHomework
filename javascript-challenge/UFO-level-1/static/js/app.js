// from data.js
var tableData = data;

// YOUR CODE HERE!
var filterButton = d3.select("#filter-btn");
var tableBody = d3.select("tbody");

// Function to handle input change
filterButton.on("click", function () {

    // Select the datetime input by user
    var dateTime = d3.select("#datetime")
    console.log(dateTime);

    var dateTimeValue = dateTime.property("value");
    console.log(dateTimeValue);

    // Filter data by datetime
    var filteredData = tableData.filter(each => each.datetime === dateTimeValue);
    console.log(filteredData);

    // Clear table contents
    tableBody.html("");
    var tableRow = tableBody.append("tr")
    // Append contents from on search data
    tableRow.append("td").text(data.map(each => each.datetime));
    tableRow.append("td").text(data.map(each => each.city));
    tableRow.append("td").text(data.map(each => each.state));
    tableRow.append("td").text(data.map(each => each.country));
    tableRow.append("td").text(data.map(each => each.shape));
    tableRow.append("td").text(data.map(each => each.durationMinutes));
    tableRow.append("td").text(data.map(each => each.comments));
});