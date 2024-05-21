def calculate_measurements(measurements):
    try:
        valid_measurements = []
        for value in measurements:
            if isinstance(value, (int, float, str)) and str(value).replace(".", "").isdigit():
                valid_measurements.append(float(value))
        if not valid_measurements:
            print("Cannot calculate average.")
            return None
        total = sum(valid_measurements)
        average = total / len(valid_measurements)
        return average
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None
measurements = [5, 20, "melis", "15.0", 16]
result = calculate_measurements(measurements)
if result is not None:
    print(f"The average measurement is {result}")