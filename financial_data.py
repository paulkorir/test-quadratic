import sys
import json

def main():
    with open("CIK0000320193.json") as f:
        data = json.load(f)

    for item, value in data.items():
        if isinstance(value, int):
            print(f"{item}: {value}")
        elif isinstance(value, str):
            print(f"{item}: {value}")
        else:
            print(f"{item} has {len(value)} values with keys {list(value.keys())}")


    # inspect the dei
    print(data['facts']['dei'])
    return 0


if __name__ == '__main__':
    sys.exit(main())