# Generate parts to match a given total
import random
import pandas as pd

def break_down_number(target_number, num_parts: int):
    # Initialize parts with zeros
    parts = [0 for _ in range(num_parts)]

    if not target_number.isnumeric():
        return parts

    target_number = int(target_number)
    # Iterate until the correct total is achieved
    while sum(parts) != target_number:
        # Calculate the difference between the current sum and the target_number
        diff = target_number - sum(parts)
        
        # Randomly select an index
        index = random.randint(0, num_parts - 1)
        
        # Generate a random value between 0 and the remaining difference, inclusive
        increment = random.randint(0, min(5 - parts[index], diff))
        
        # Update the selected part
        parts[index] += increment

    return parts

def main():
    done = False

    while not done:
        filename = input('Enter filename: ')

        try:
            input_df = pd.read_csv(filename, header=None)
            done = True
        except FileNotFoundError as e:
            print("Incorrect filename:", e)
        except Exception as e:
            print("Needs proper csv file:", e)


    output_df = pd.DataFrame(columns=[0, 1, 2, 3, 4])
    # print(output_df)

    for ind, row in input_df.iterrows():
        target_number = str(row[0])
        parts = break_down_number(target_number, num_parts=4)
        parts.append(target_number)
        output_df.loc[len(output_df)] = parts

    print(output_df.head())
    output_df.to_csv(f'output_{filename}', index=None, header=False)
    print(f'output_{filename} generated')


if __name__ == '__main__':
    main()

