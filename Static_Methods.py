class TemperatureConverter:
    # Define a static method that converts Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Apply the conversion formula: (°C × 9/5) + 32 = °F
        return (c * 9/5) + 32

# Example usage:
celsius = 100  # Temperature in Celsius
# Call the static method directly using the class name (no need to create an instance)
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)

# Print the result
print(f"{celsius}°C is equal to {fahrenheit}°F")
