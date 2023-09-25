from components.plots import *

Graph_types = [
    {"label": "Line Graph", "value": 0},
    {"label": "Scatter Plot", "value": 1},
    {"label": "Histogram", "value": 2},
    {"label": "Density Plot", "value": 3},
    {"label": "Correlation Plot", "value": 4},
    {"label": "Pie Chart", "value": 5},
    {"label": "Bar Chart", "value": 6},
    {"label": "Violin Plot", "value": 7},
    {"label": "Box Plot", "value": 8},
    {"label": "Count heatmap", "value": 9},
]

Graphs = [
    plot_line,
    plot_scatter,
    plot_hist,
    plot_dist,
    plot_corr,
    plot_pie,
    plot_bar,
    plot_violin,
    plot_box,
    plot_count,
]

Graph_attributes = [
    ("X : ", "Y : ", "Color : ", "Not available"),
    ("X : ", "Y : ", "Color : ", "Size : "),
    ("X : ", "Y : ", "Color : ", "Pattern : "),
    ("X : ", "Y : ", "Color : ", "Not available"),
    ("X : ", "Not available", "Not available", "Not available"),
    ("Name : ", "Value : ", "Color : ", "Not available"),
    ("X : ", "Y : ", "Color : ", "Pattern : "),
    ("X : ", "Y : ", "Color : ", "Not available"),
    ("X : ", "Y : ", "Color : ", "Not available"),
    ("X : ", "Y : ", "Not available", "Not available"),
]
