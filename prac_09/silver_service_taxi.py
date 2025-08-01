from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi with name, fuel, and fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return fare including flagfall."""
        return super().get_fare() + self.flagfall
