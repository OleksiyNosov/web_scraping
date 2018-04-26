import os

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as figure_factory

import numpy
import pandas

laptops_filename = "laptops.csv"

datafile = pandas.read_csv(laptops_filename)
sample_data_table = figure_factory.create
