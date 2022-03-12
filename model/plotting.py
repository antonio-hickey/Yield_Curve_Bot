import plotly.graph_objects as go


class Plotting:
    def __init__(self, curves: dict, instrument: str, title: str) -> None:
        self.instrument = instrument
        self.fig = go.Figure()
        current_curve = go.Scatter(
            x=list(curves["current"].keys())[1:],
            y=list(curves["current"].values())[1:],
            mode='lines+markers',
            name=f'{list(curves["current"].values())[0]}',
            line=dict(color='firebrick'),
        )
        previous_curve = go.Scatter(
            x=list(curves["previous"].keys())[1:],
            y=list(curves["previous"].values())[1:],
            mode='lines+markers',
            name=f'{list(curves["previous"].values())[0]}',
            line=dict(color='cornflowerblue'),
            fill='tonexty',
            line_color='darkslategrey',
        )
        self.fig.add_traces([current_curve, previous_curve])
        self.fig.update_layout(
            title=title,
            xaxis_title='Maturity',
            yaxis_title='Interest Rate',
            title_font_size=24,
            title_x=0.5,
            legend={'traceorder': 'normal'},
            font=dict(
              family="Trebuchet MS",
              size=14,
              color="black",
            ),
        )

    def pointing_wojak(self) -> None:
        """Renders plot with pointing wojaks."""
        self.fig.add_layout_image(
            dict(source="https://raw.githubusercontent.com/antonio-hickey/Yield_Curve_Bot/main/assets/images/wojaks/pointing.png",
                 xref="paper", yref="paper",
                 x=1, y=0,
                 sizex=0.7, sizey=0.7,
                 xanchor="right", yanchor="bottom"),
        )
        self.fig.write_image(f"assets/images/plots/{self.instrument}.png")
