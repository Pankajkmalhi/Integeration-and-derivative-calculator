import sympy as sp

def main():
    print("Welcome to the Differentiation and Integration Calculator!")
    while True:
        print("\nChoose an option:")
        print("1. Differentiate")
        print("2. Integrate")
        print("3. Differentiate and Integrate")
        print("4. Exit")
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 4:
            print("Goodbye!")
            break

        function_str = input("Enter the function: ")
        x = sp.symbols('x')
        function = sp.sympify(function_str)

        if choice == 1:
            derivative = sp.diff(function, x)
            print(f"The derivative of {function_str} is: {derivative}")

        elif choice == 2:
            integral = sp.integrate(function, x)
            print(f"The indefinite integral of {function_str} is: {integral}")

        elif choice == 3:
            derivative = sp.diff(function, x)
            integral = sp.integrate(function, x)
            print(f"The derivative of {function_str} is: {derivative}")
            print(f"The indefinite integral of {function_str} is: {integral}")

if __name__ == "__main__":
    main()
