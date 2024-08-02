def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
# square_target: The number for which you want to find the square root.
# tolerance (optional): The acceptable difference between the square of the approximate root value and the actual target value (default is 1e-7). The tolerance 1e-7 implies that the solution will be accurate to within 0.0000001 of the true value and is a good default choice that balances accuracy and performance.
# max_iterations (optional): The maximum number of iterations to perform (default is 100). If the method doesn't converge within this limit, you'll assume the solution is not found.
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root


square_root_bisection(16)

                