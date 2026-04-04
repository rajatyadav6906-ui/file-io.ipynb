#    pr 8


import numpy as np

class NumpyArrayAnalyzer:
    def __init__(self):
        # Stores the current working array
        self.array = None
        # Stores the original array (before modification)
        self.original_array = None

    def create_1D_array(self):
        """Create a 1D NumPy array from user input"""
        try:
            elements = input("Enter elements (space-separated): ")
            self.array = np.array(list(map(int, elements.split())))
            self.original_array = self.array.copy()  # Save original
            print("1D array created:", self.array)
        except ValueError:
            print("Error: Please enter valid integers.")

    def create_2D_array(self):
        """Create a 2D NumPy array with specified rows and columns"""
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            elements = input(f"Enter {rows * cols} elements (space-separated): ")
            data = list(map(int, elements.split()))
            if len(data) != rows * cols:
                print("Error: Incorrect number of elements.")
                return
            self.original_array = np.array(data).reshape(rows, cols)
            self.array = self.original_array.copy()
            print("2D array created:\n", self.original_array)
        except ValueError:
            print("Error: Please enter valid integers.")

    def create_3D_array(self):
        """Create a 3D NumPy array with specified dimensions"""
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            layers = int(input("Enter number of layers: "))
            total = rows * cols * layers
            elements = input(f"Enter {total} elements (space-separated): ")
            data = list(map(int, elements.split()))
            if len(data) != total:
                print(f"Error: You must enter exactly {total} elements.")
                return
            self.array = np.array(data).reshape(rows, cols, layers)
            self.original_array = self.array.copy()
            print("3D array created:\n", self.array)
        except ValueError:
            print("Error: Please enter valid integers.")

    # =================== STATISTICS METHODS ====================
    def mean(self):
        """Calculate mean"""
        if self.array is not None:
            print("Mean:", np.mean(self.array))

    def median(self):
        """Calculate median"""
        if self.array is not None:
            print("Median:", np.median(self.array))

    def std_dev(self):
        """Calculate standard deviation"""
        if self.array is not None:
            print("Standard deviation:", np.std(self.array))

    def variance(self):
        """Calculate variance"""
        if self.array is not None:
            print("Variance:", np.var(self.array))

    def sum(self):
        """Calculate sum of original array"""
        if self.original_array is not None:
            print("Sum:", np.sum(self.original_array))

    # =================== OTHER OPERATIONS ====================
    def sort(self):
        """Sort the array"""
        if self.original_array is not None:
            print("Sorted array:\n", np.sort(self.original_array, axis=None))

    def filter_even(self):
        """Filter even numbers"""
        if self.array is not None:
            print("Even numbers:", self.array[self.array % 2 == 0])

    def search(self):
        """Search for a value in the array"""
        if self.original_array is not None:
            try:
                value = int(input("Enter a value to search: "))
                result = np.where(self.original_array == value)
                print(f"Value found at: {result}")
            except ValueError:
                print("Please enter a valid integer.")

    def split_array(self):
        """Split array into equal parts"""
        if self.original_array is not None:
            try:
                num = int(input("Enter the number of splits: "))
                splits = np.array_split(self.original_array, num)
                print("Array split into:")
                for i, s in enumerate(splits):
                    print(f"Part {i + 1}:\n{s}")
            except ValueError:
                print("Please enter a valid number.")

    def combine_vertical(self):
        """Stack array vertically"""
        try:
            elements = input("Enter elements to stack vertically (space-separated): ")
            new_array = np.array(list(map(int, elements.split()))).reshape(self.original_array.shape)
            combined = np.vstack((self.original_array, new_array))
            print("Vertically combined array:\n", combined)
        except Exception as e:
            print("Error:", e)

    def combine_horizontal(self):
        """Stack array horizontally"""
        try:
            elements = input("Enter elements to stack horizontally (space-separated): ")
            new_array = np.array(list(map(int, elements.split()))).reshape(self.original_array.shape)
            combined = np.hstack((self.original_array, new_array))
            print("Horizontally combined array:\n", combined)
        except Exception as e:
            print("Error:", e)

    # =================== ARITHMETIC OPERATIONS ====================
    def addition_array(self):
        """Add another array to the current array"""
        try:
            elements = input("Enter elements to add (space-separated): ")
            new_array = np.array(list(map(int, elements.split()))).reshape(self.array.shape)
            result = self.array + new_array
            print("Addition result:\n", result)
        except Exception as e:
            print("Error:", e)

    def subtraction_array(self):
        """Subtract another array from the current array"""
        try:
            elements = input("Enter elements to subtract (space-separated): ")
            new_array = np.array(list(map(int, elements.split()))).reshape(self.array.shape)
            result = self.array - new_array
            print("Subtraction result:\n", result)
        except Exception as e:
            print("Error:", e)

    def multiplication_array(self):
        """Multiply another array with the current array"""
        try:
            elements = input("Enter elements to multiply (space-separated): ")
            new_array = np.array(list(map(int, elements.split()))).reshape(self.array.shape)
            result = self.array * new_array
            print("Multiplication result:\n", result)
        except Exception as e:
            print("Error:", e)

    def divided_array(self):
        """Divide current array by another array"""
        try:
            elements = input("Enter elements to divide (space-separated): ")
            new_array = np.array(list(map(int, elements.split()))).reshape(self.array.shape)
            result = self.array / new_array
            print("Division result:\n", result)
        except Exception as e:
            print("Error:", e)

# ========================= MAIN DRIVER CODE =========================

ca = NumpyArrayAnalyzer()

print("Welcome to the NumPy Analyzer!")
print("=" * 40)

while True:
    print("\nSelect an sub_option:")
    print("1. Create NumPy array")
    print("2. Perform mathematical operation")
    print("3. Combine or split array")
    print("4. Search, sort, or filter array")
    print("5. Compute aggregate and statistics")
    print("6. Exit")

    try:
        main_sub_option = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    match main_sub_option:
        case 1:
            while True:
                print("\nSelect the type of array to create:")
                print("1. 1D array")
                print("2. 2D array")
                print("3. 3D array")
                print("4. Go to main menu")

                try:
                    array_sub_option = int(input("Enter your sub_option: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                match array_sub_option:
                    case 1:
                        ca.create_1D_array()
                    case 2:
                        ca.create_2D_array()
                    case 3:
                        ca.create_3D_array()
                    case 4:
                        break

        case 2:
            while True:
                print("\nPerform mathematical operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Go to main menu")

                try:
                    math_sub_option = int(input("Enter your sub_option: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                match math_sub_option:
                    case 1:
                        ca.addition_array()
                    case 2:
                        ca.subtraction_array()
                    case 3:
                        ca.multiplication_array()
                    case 4:
                        ca.divided_array()
                    case 5:
                        break

        case 3:
            while True:
                print("\nCombine and split array:")
                print("1. Combine the array")
                print("2. Split the array")
                print("3. Go to main menu")

                try:
                    combine_sub_option = int(input("Enter your sub_option: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                match combine_sub_option:
                    case 1:
                        while True:
                            print("Combine the array: ")
                            print("1. Vertically concatenate")
                            print("2. Horizontally concatenate")
                            print("3. Go to main menu")

                            try:
                                sub_sub_option = int(input("Enter your sub_option: "))
                            except ValueError:
                                print("Invalid input.")
                                continue

                            match sub_sub_option:
                                case 1:
                                    ca.combine_vertical()
                                case 2:
                                    ca.combine_horizontal()
                                case 3:
                                    break
                    case 2:
                        ca.split_array()
                    case 3:
                        break

        case 4:
            while True:
                print("Search, sort, and filter array:")
                print("1. Search the array")
                print("2. Sort the array")
                print("3. Filter the array (even numbers)")
                print("4. Go to main menu")

                try:
                    filter_sub_option = int(input("Enter your sub_option: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                match filter_sub_option:
                    case 1:
                        ca.search()
                    case 2:
                        ca.sort()
                    case 3:
                        ca.filter_even()
                    case 4:
                        break

        case 5:
            while True:
                print("Compute aggregate and statistics:")
                print("1. Sum")
                print("2. Mean")
                print("3. Median")
                print("4. Standard deviation")
                print("5. Variance")
                print("6. Go to main menu")

                try:
                    stats_sub_option = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                match stats_sub_option:
                    case 1:
                        ca.sum()
                    case 2:
                        ca.mean()
                    case 3:
                        ca.median()
                    case 4:
                        ca.std_dev()
                    case 5:
                        ca.variance()
                    case 6:
                        break

        case 6:
            print("Thank you for using NumPy Analyzer! Goodbye.")
            break