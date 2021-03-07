import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.H1(children="Hello Dash",
            style= {
                'textAlign':'center',
                'color':'#ff0000'
            }

            ),
    html.Div( children ="Dash - a Data product develompent framework from ploty",
              style={
                'textAlign':'center',
                'color':'#ff0000'

              }

              ),

    dcc.Graph(
        id='simple-graph',
        figure={
            'data': [
                {'x': [4, 5, 6], 'y': [12, 16, 18], 'type': 'bar', 'name': 'First Chart'},
                {'x': [10, 11, 12], 'y': [13, 14, 15], 'type': 'bar', 'name': 'First Chart'}
            ],
            'layout': {
                'plot_bgcolor' : '#D3D3D3',
                'paper_bgcolor' : '#D3D3D3',
                'font' : {
                    'color' : 'ff0000'
                },
                'title': 'Simple Chart'
            }
        }
    )

])

if __name__ == '__main__':
    print(help(html.Div))
    app.run_server(debug=True, port=4050)
