from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None

    total_cost = 0

if __name__ == '__main__':
main()