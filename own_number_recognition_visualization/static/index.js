import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

const display = document.getElementById("display")
console.log(d3)

const originalLabelsRequest = await fetch("/original").then((response) => response.json())
const tsneResultsRequest = await fetch("/tsne").then((response) => response.json())
const predictionLabelsRequest = await fetch("/prediction").then((response) => response.json())

const [
    originalLabels,
    tsneResults,
    predictionLabels
] = await Promise.all([originalLabelsRequest, tsneResultsRequest, predictionLabelsRequest])

const svg = d3.select("svg")

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

const bcrect = svg.node().getBoundingClientRect();

const show = async (idx) => {
    document.getElementById('display').src = "";
    fetch(`/image/${idx}`)
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

const labelMap = [
    "#ff0000",
    "#00ff00",
    "#0000ff",
    "#f0f0f0",
    "#ff0000",
    "#ff0000",
    "#ff0000",
    "#ff0000",
    "#ff0000",
    "#ff0000",
]

// Add dots
svg.append('g')
    .selectAll("dot")
    .data(tsneResults)
    .enter()
    .append("circle")
        .attr("cx", function (d) { return bcrect.width / 2 + x(d); } )
        .attr("cy", function (d) { return bcrect.height / 2 + y(d); } )
        .attr("r", 0.75)
        .style("fill", (_, i) => d3.hsl(originalLabels[i] * 360 / 10 , 1, 0.5))
        .on("mouseover", function(event, d) {
            d3.selectAll('circle').style("fill", (d, i) => d3.hsl(originalLabels[i] * 360 / 10 , 1, 0.5)).style("z-index", "1")
            d3.select(this).style("fill", "#ff0000")
        })
        .on("click", function(event, d) {
            console.log({ d });
            show(data.indexOf(d))
        });;

const showOriginal = document.getElementById('showOriginal');
showOriginal.addEventListener('click', () => {
    svg.selectAll('circle').each((datum, index, nodes) => {
        d3.select(nodes[index]).style("fill", d3.hsl(originalLabels[index] * 360 / 10 , 1, 0.5))
    })
});


const showPrediction = document.getElementById('showPrediction');
showOriginal.addEventListener('click', () => {
    svg.selectAll('circle').each((datum, index, nodes) => {
        d3.select(nodes[index]).style("fill", d3.hsl(predictionLabels[index] * 360 / 10 , 1, 0.5))
    });
    console.log('test')
});
