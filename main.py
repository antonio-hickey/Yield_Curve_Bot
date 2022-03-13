from model.plotting import Plotting
from model.text import Render_Text
from model.twitter import Twitter_Client
from model.us_treasury import UST

UST_SPOT: str = "UST_Spot"
Title: str = "How the market moved the Spot U.S Treasury curve today..."


def UST_Spot_Curve(title: str = Title) -> None:
    """Tweet todays UST Spot Curve Observation."""

    # Curve data
    curves: dict = {}
    curves["current"] = UST().current_curve()
    curves["previous"] = UST().previous_curve()

    # Plotting curves
    Plotting(curves, UST_SPOT, title).pointing_wojak()

    # Observation
    observation = Render_Text(
        curves["current"], curves["previous"],
    ).run()

    # Tweet the observation
    Twitter_Client().create_tweet_with_media(
        text_content=observation,
        media_path="assets/images/plots/UST_Spot.png",
    )


if __name__ == "__main__":
    UST_Spot_Curve()
