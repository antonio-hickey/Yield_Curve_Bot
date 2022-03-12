import requests as req  # type: ignore


class UST:
    def __init__(self) -> None:
        self.URL = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2022"  # noqa: E501
        self._fetch()

    def _fetch(self) -> None:
        """Fetches the URL returning it's response as a list of rows."""
        response = (req.get(self.URL).content).decode("utf-8")
        self.response = response.split("\n")
        self.target: int = self.find_table()

    def find_table(self) -> int:
        """Finds the target table."""
        curve = self.response
        for i, j in enumerate(curve):
            if "</table>" in j:
                return int(i)
        return -1

    def parse_date(self, unparsed: str) -> str:
        """Parse the date string into a desired string format."""
        date_pre = unparsed[unparsed.find("datetime"):]
        start, end = date_pre.find(">") + 1, date_pre.find("<")
        return date_pre[start:end]

    def parse_yields(self, unparsed: str) -> float:
        """Parse yield string to float."""
        return float(unparsed[unparsed.find(">")+1:unparsed.find(".")+3])

    def as_dict(self, curve: list) -> dict:
        """Converts curve array to hashmap."""
        return {
            "date": self.parse_date(curve[0]),
            "1 Month": self.parse_yields(curve[9]),
            "2 Month": self.parse_yields(curve[10]),
            "3 Month": self.parse_yields(curve[11]),
            "6 Month": self.parse_yields(curve[12]),
            "1 Year": self.parse_yields(curve[13]),
            "2 Year": self.parse_yields(curve[14]),
            "3 Year": self.parse_yields(curve[15]),
            "5 Year": self.parse_yields(curve[16]),
            "7 Year": self.parse_yields(curve[17]),
            "10 Year": self.parse_yields(curve[18]),
            "20 Year": self.parse_yields(curve[19]),
            "30 Year": self.parse_yields(curve[20]),
        }

    def find_cur_curve(self) -> list:
        """Finds the current curve inside the table."""
        return self.response[self.target-23:self.target-2]

    def current_curve(self) -> dict:
        """Returns the current U.S Treasury curve."""
        return self.as_dict(
            self.find_cur_curve(),
        )

    def find_prev_curve(self) -> list:
        """Finds the previous curve inside the table."""
        return self.response[self.target-46:self.target-23]

    def previous_curve(self) -> dict:
        """Returns the previous U.S Treasury curve."""
        return self.as_dict(
            self.find_prev_curve(),
        )
