from unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar by drive it multiple times."""
    test_car = UnreliableCar("TestCar", 100, 30)  # 30% reliable
    total_distance = 0

    for i in range(10):
        distance = test_car.drive(10)
        print(f"Attempt {i+1}: Drove {distance}km")
        total_distance += distance

    print(f"Total distance driven: {total_distance}km")
    print(test_car)

main()
