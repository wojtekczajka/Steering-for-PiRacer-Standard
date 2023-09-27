import argparse
import vehicle_steering

def main():
    parser = argparse.ArgumentParser(description="Control the vehicle's steering and movement.",
                                     usage="python3 steer.py <action> [--value <value>]")
    parser.add_argument("action", choices=["start", "stop", "turn_left", "turn_right", "center", "drive_forward", "drive_backward"],
                        help="Action to perform")
    parser.add_argument("--value", type=int, help="Value for turning or driving (0 to 100)")

    args = parser.parse_args()
    if args.action == "start":
        vehicle_steering.start_vehicle()
    elif args.action == "stop":
        vehicle_steering.stop_vehicle()
    elif args.action == "turn_left" and args.value is not None:
        vehicle_steering.turn_vehicle_left(args.value)
    elif args.action == "turn_right" and args.value is not None:
        vehicle_steering.turn_vehicle_right(args.value)
    elif args.action == "center":
        vehicle_steering.center_steering()
    elif args.action == "drive_forward" and args.value is not None:
        vehicle_steering.drive_forward(args.value)
    elif args.action == "drive_backward" and args.value is not None:
        vehicle_steering.drive_backward(args.value)
    else:
        print("Invalid action or missing value.")

if __name__ == "__main__":
    main()
