# main.py

try:
    from .parking_system import SmartParking
    from .config import PARKING_SLOTS
except ImportError:
    from parking_system import SmartParking
    from config import PARKING_SLOTS


def main():

    parking = SmartParking(PARKING_SLOTS)

    while True:

        print("\n===== SMART PARKING SYSTEM =====")
        print("1. Allocate Slot")
        print("2. Free Slot")
        print("3. Show Parking Status")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            vehicle = input("Enter Vehicle Number: ")

            result = parking.allocate_slot(vehicle)

            print(result)


        elif choice == "2":

            slot = input("Enter Slot ID: ")

            result = parking.free_slot(slot)

            print(result)


        elif choice == "3":

            parking.show_status()


        elif choice == "4":

            print("System Closed")
            break


        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()