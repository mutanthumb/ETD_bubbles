# ETD_viz
Code associated with ETD Visualization poster presented at Open Repositories 2015

Summary of the project: 
Montana State University recently digitized 5,500 Theses and Dissertations. These, added to the papers we have been collecting digitally since 2004, represent the bulk of our repository: 7274 electronic thesis and dissertation(ETDs).  In order to more fully understand this collection we have treated the associated metadata as a dataset.  ETDs are often overlooked as necessary but unimportant items. We believe that visualization can add value to ETD collections just like a “regular” dataset to help us understand and share the impact of our graduate work.

In the resulting “bubble” visualization each bubble indicates an ETD the location indicates publication year and the bubble size indicates relative number of ETDs published in a given year.

D3.js was the main engine behind this visualization, it was based on Asif Rahman's "Punchcard visualization using D3.js"  
See http://asifr.com/punchcard-visualization-using-d3js.html for reference.

After much munging and whatnot the .csv was put into the correct nested json format with nested_dict_csv.py
Sample csv and json files have been attached here as well.

End result of the project: http://www.lib.montana.edu/~susan/etd_bubbles.html

My plan is to improve the js within the HTML file to do the csv to nested json internally to eliminate a step. Other improvements will be to streamline the export and data munging process as well.

Please feel free to contact me with any questions.

