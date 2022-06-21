import time

import pytest
import softest
from Utilities.Utils import utils
from Pages.test_flight import launchpages
from Base.base import BaseDriver
@pytest.mark.usefixtures("setup")
class TestCaseFlights(softest.TestCase):
    def test_flight(self):
        lp=launchpages(self.driver)
        # lp.depart_from()
        # lp.Going_to()
        # lp.departure_date()
        # lp.search_button()
        lp.search_filter()
        bd=BaseDriver(self.driver)
        bd.windowScroll()
        lp.search_stop()



