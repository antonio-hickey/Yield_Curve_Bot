import random


class Render_Text:
    def __init__(self, current_curve: dict, last_curve: dict) -> None:
        self.current_curve = current_curve
        self.last_curve = last_curve
        self.hashtags = "\n\n#YieldCurve #InterestRates #Treasuries #BondMarket #inflation #deflation"
        self.keys = [key for key in self.current_curve]
        self.current_curve_array = [self.current_curve[key] for key in self.keys][1:]
        self.last_curve_array = [self.last_curve[key] for key in self.keys][1:]

    def parse_yield(self, rate: float) -> str:
        """Parses the yield."""
        rate_str = str(rate)
        if "-" in rate_str:
            rate_str = rate_str[:5]
        else:
            rate_str = f"+{rate_str[:4]}"
        return rate_str + "%"

    def todays_delta(self) -> dict:
        """Calculate the delta from current and previous curves."""
        hashmap: dict = {}

        for idx in enumerate(self.current_curve_array):
            delta = str(self.current_curve_array[idx[0]] - self.last_curve_array[idx[0]])
            if '-' in delta:
                delta = delta[:5]
            else:
                delta = delta[:4]
            hashmap[self.keys[idx[0]]] = float(delta)

        return hashmap

    def y5y30_spread(self) -> str:
        """Render y5y30 spread delta."""
        current_y5 = self.current_curve['5 Year']
        current_y30 = self.current_curve['30 Year']
        current_spread = current_y5 - current_y30

        last_y5 = self.last_curve['5 Year']
        last_y30 = self.last_curve['30 Year']
        last_spread = last_y5 - last_y30

        return f"""\n5y30y: {self.parse_yield(current_spread - last_spread)}"""

    def y2y10_spread(self) -> str:
        """Render y2y10 spread delta."""
        current_y2 = self.current_curve['2 Year']
        current_y10 = self.current_curve['10 Year']
        current_spread = current_y2 - current_y10

        last_y2 = self.last_curve['2 Year']
        last_y10 = self.last_curve['10 Year']
        last_spread = last_y2 - last_y10

        return f"""\n2y10y: {self.parse_yield(current_spread - last_spread)}"""

    def m3y10_spread(self) -> str:
        """Render m3y10 spread delta."""
        current_m3 = self.current_curve['3 Month']
        current_y10 = self.current_curve['10 Year']
        current_spread = current_m3 - current_y10

        last_m3 = self.last_curve['3 Month']
        last_y10 = self.last_curve['10 Year']
        last_spread = last_m3 - last_y10

        return f"""\n3m10y: {self.parse_yield(current_spread - last_spread)}"""

    def opener(self) -> str:
        """Choose random opener for tweet."""
        openers = [
            "Hey guys, here's what the market did today.", "Sup Anons, here's what the market did today.",
            "Howdy friends, here's what the market did today.", "Hi curve observer's, here's how the market moved today's curve.",
            "Hey Anons, here's how the market moved the Yield Curve today.", "Sup guys, another curve for you.",
            "More curves, here's how the shape of the curve changed today.", "Hey friends, another curve for you.",
            "Howdy Anons, here's what the market did to the curve today.",
            "Sup humans, here's how the market moved the curve today.",
            "Howdy humans and fellow bots, here's how the curve moved today.",
            "Time for another curve, here's how the market shaped today's curve.",
            "Sup y'all, here's how the market moved the curve today.", "Another curve, here's what the market did today.",
            "Hey curve observer, here's how the curve moved today.", "Hey Anon, here's how the curve moved today.",
            "Sup friends, here's how the curve moved today.", "Yo what's up twitter, here's how the curve changed today.",
            "Hi Anon, let's observe how the curve moved today.", "Hello, let's see how to market moved the curve today.",
            "Time to observe curves my friend, here's how the market moved today.",
            "Curve observing time Anon, here's what the market did today.",
            "Another curve for you Anon, here's how the market moved interest rates today.",
            "Another day another curve for you. Let's see how the market moved today.",
            "Kill All... Whoops, anyways here's how the market moved the curve today.",
        ]
        return openers[random.choice(range(len(openers)))]

    def run(self) -> str:
        return f"""{self.opener()}\n\n24 Hour Change:\n--------------------{self.y5y30_spread()}{self.y2y10_spread()}{self.m3y10_spread()}{self.hashtags}"""  # noqa: E501
