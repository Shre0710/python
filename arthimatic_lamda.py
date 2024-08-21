

addition_fun = lambda x, y: x + y
result = addition_fun(5, 3)
print("Addition (5 + 3):", result)


sub_fun = lambda x, y: x - y
result = sub_fun(5, 3)
print("subtraction(5 - 3):", result)


mul_fun = lambda x, y: x * y
result = mul_fun(5, 3)
print("multiplication (5 * 3):", result)


div_operation = lambda x, y: x / y if y != 0 else "Division by zero is not allowed"
result1 = div_operation(10, 2)
result2 = div_operation(10, 0)
print("Division (10 / 2):", result1)
print("Division (10 / 0):", result2)