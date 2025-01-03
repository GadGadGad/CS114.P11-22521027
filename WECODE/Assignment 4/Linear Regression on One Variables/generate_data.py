import random

# Function to generate linear data with noise
def generate_linear_data_with_noise():
    num_entries = random.randint(10, 20)
    data = []
    
    # Linear slope and initial value for float parts
    slope = random.uniform(0.01, 0.05)
    float_value = random.uniform(1.0, 3.0)  # Starting float value

    for i in range(num_entries):
        # Integer part with small random noise
        integer_part = 20000000 + i + random.randint(-5, 5)  # Add noise to the integer part
        
        # Increment float part based on the slope and add noise
        float_value = round(float_value + slope, 5)
        float_noise = random.uniform(-0.1, 0.1)  # Noise for the float part
        noisy_float_value = round(float_value + float_noise, 5)
        
        data.append(f"{integer_part},{noisy_float_value}")
        
    return data


iterations = 10

for i in range(2, iterations + 1):
    # Generate the linear data with noise
    generated_data = generate_linear_data_with_noise()

    # Save the generated data to a .txt file named input[i].txt
    file_name = f"inputs/input{i}.txt"  # Name of the output file

    with open(file_name, "w") as file:
        for entry in generated_data:
            file.write(entry + "\n")  # Write each entry on a new line

    print(f"Data saved to {file_name}.")
