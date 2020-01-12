// from data.js
var tableData = data;

// YOUR CODE HERE!
var filterButton = d3.select("#filter-btn");
// Function to handle input change
filterButton.on("click", function () {
    // Select the table body
    var tableBody = d3.select("tbody");
    // Select the datetime input by user
    var dateTime = d3.select("#datetime")
    console.log(dateTime);

    var dateTimeValue = dateTime.property("value");
    console.log(dateTimeValue);

    // Filter data by input datetime
    var filteredData = tableData.filter(each => each.datetime === dateTimeValue);
    console.log(filteredData);

    // Clear table contents
    tableBody.html("");
    filteredData.forEach(each => {
        var tableRow = tableBody.append("tr")
        // Append contents from filtered data
        tableRow.append("td").text(each.datetime);
        tableRow.append("td").text(each.city);
        tableRow.append("td").text(each.state);
        tableRow.append("td").text(each.country);
        tableRow.append("td").text(each.shape);
        tableRow.append("td").text(each.durationMinutes);
        tableRow.append("td").text(each.comments);
    });
});