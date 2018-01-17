import plotly
from plotly.graph_objs import *
plotly.tools.set_credentials_file(username='crisvdn', api_key='yKPOxMazWerZBxnCkqji')

data = Data([
    Scatter(
        x=[1, 2],
        y=[3, 4]
    )
])

plot_url = plotly.offline.plot(data, filename='my plot')
