import pandas as pd

def main():
    # Create a DataFrame with dummy data
    data = {'name': ['Vivek', 'Krishna', 'Ketan Rai'],
            'marks': [85, 90, 88],
            'age': [20, 21, 22]}
    df = pd.DataFrame(data)

    # Add a new column "admission no."
    df['admission no.'] = ['650', '649', '700']

    # Print the DataFrame
    print("DataFrame with new column 'admission no.':")
    print(df)

if __name__ == "__main__":
    main()
