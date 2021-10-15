from application import app
from flask import render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
from copy_of_eda_1 import fig1,fig2,fig3,fig4,fig5,predictOutput

@app.route('/')
def index():
    # Graph One
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph two
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph three
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph three
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph three
    graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graph1JSON=graph1JSON,  graph2JSON=graph2JSON, graph3JSON=graph3JSON, graph4JSON=graph4JSON, graph5JSON=graph5JSON)


@app.route('/',methods=['POST'])
def preds():
    if request.method == 'POST':
    #   year = request.body["year"]
    #   month = request.body["month"]
      print(request)
      print(request.json)
      print(list(request.json.values()))
      return predictOutput(inputs=list(request.json.values()))
