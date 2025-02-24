import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";
const svg = d3.select("#my_please_select_svg")

const x = (row) => row[0]
const y = (row) => row[1]




function zoomed(event) {
    const { transform } = event;
    svg.select('g').attr("transform", transform);
}

const zoom = d3.zoom()
    .scaleExtent([1, 10]) // Set the minimum and maximum zoom scale
    .on("zoom", zoomed);   // Define the zoom event handler

svg.call(zoom);

tsneResults = window.tsneResults;
originalLabels = window.originalLabels;
const bcrect = svg.node().getBoundingClientRect();
console.log({
    tsneResults,
    originalLabels,
})

const show = async (idx) => {
    fetch(`http://127.0.0.1:8000/image/${idx}`)
        .then(response => {
            // Convert the response to a blob
            return response.blob();
        })
        .then(blob => {
            // Create a URL for the blob
            const imageUrl = URL.createObjectURL(blob);

            // Set the image source to the URL
            document.getElementById('display').src = imageUrl;
        })
        .catch(error => {
            console.error('Error fetching image:', error);
        });
}

const index = d3.local();
// Add dots
svg.append('g')
    .selectAll("dot")
    .data(tsneResults)
    .enter()
    .append("circle")
        .attr("cx", function (d) { return bcrect.width / 2 + x(d); } )
        .attr("cy", function (d) { return bcrect.height / 2 + y(d); } )
        .each(function(d, i) {
            index.set(this, i);            // Store index in local variable.
        })
        .attr("r", 0.75)
        .style("fill", (_, i) => d3.hsl(originalLabels[i] * 360 / 10 , 1, 0.5))
        .on("mouseover", function(event, d) {
            svg.selectAll('circle').classed('hovered', (_, i) => i === tsneResults.indexOf(d))
        })
        .on("click", function(event, d) {
            console.log({ d });
            show(index.get(this))
        });