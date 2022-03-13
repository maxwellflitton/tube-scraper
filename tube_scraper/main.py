from enum import Enum
from typing import Optional, Dict

import requests
from bs4 import BeautifulSoup as bs


class TubeLineEnum(Enum):
    LONDON_OVERGROUND = "London Overground"
    HAMMERSMITH_AND_CITY = "Hammersmith & City"
    NORTHERN = "Northern"
    PICCADILLY = "Piccadilly"
    BAKERLOO = "Bakerloo"
    CENTRAL = "Central"
    JUBILEE = "Jubilee"
    METROPOLITAN = "Metropolitan"
    VICTORIA = "Victoria"
    DISTRICT = "District"
    CIRCLE = "Circle"
    WATERLOO_AND_CITY = "Waterloo & City"
    DLR = "DLR"


class TubeStatus:

    LINES = ["London Overground", "Hammersmith & City", "Northern", "Piccadilly", "Bakerloo", "Central",
             "Jubilee", "Metropolitan", "Victoria", "District", "Circle", "Waterloo & City", "DLR"]
    URL = "https://tfl.gov.uk/tube-dlr-overground/status/"

    def __init__(self) -> None:
        self._cached_data: Optional[Dict[str, str]] = None

    def _get_data(self) -> None:
        req = requests.get(self.URL)

        status_soup = bs(req.content, "html.parser")
        station_output = status_soup.find_all("span", class_="service-name")
        status_output = status_soup.find_all("span", class_="disruption-summary")
        counter = 0
        status_dict = {}

        for _ in station_output:
            station_key = station_output[counter].find('span').contents[0]
            status_value = status_output[counter].find('span').contents[0].replace("\n", "")
            if station_key in self.LINES:
                status_dict[station_key] = status_value[:-1]
            else:
                pass
            counter = counter + 1
        self._cached_data = status_dict

    def get_line_status(self, line: TubeLineEnum) -> str:
        return self.cached_data[line.value]

    @property
    def cached_data(self) -> Dict[str, str]:
        if self._cached_data is None:
            self._get_data()
        return self._cached_data


if __name__ == "__main__":
    test = TubeStatus()
    print(test.cached_data)
    print(test.get_line_status(line=TubeLineEnum.DISTRICT))
