from coffee import Coffee
from customer import Customer

def run_tests():
    print("Running tests...\n")

    # Test Coffee
    print("Testing Coffee...")
    try:
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        assert coffee1.name == "Latte"
        assert coffee2.name == "Espresso"
        print("Coffee creation tests passed.")
    except ValueError as e:
        print(f"Coffee test failed: {e}")

    # Test Customer
    print("\nTesting Customer...")
    try:
        customer1 = Customer("John Doe")
        customer2 = Customer("Jane")
        assert customer1.name == "John Doe"
        assert customer2.name == "Jane"
        print("Customer creation tests passed.")
    except ValueError as e:
        print(f"Customer test failed: {e}")

    # Test Orders
    print("\nTesting Orders...")
    try:
        order1 = customer1.create_order(coffee1, 5.0)
        order2 = customer2.create_order(coffee2, 3.5)
        
        assert order1.price == 5.0
        assert order1.coffee.name == "Latte"
        assert order1.customer.name == "John Doe"
        assert coffee1.num_orders() == 1
        assert coffee1.average_price() == 5.0
        
        print("Order creation tests passed.")
    except ValueError as e:
        print(f"Order test failed: {e}")

    # Display final results
    print("\nFinal Results:")
    print(f"{coffee1.name} has been ordered {coffee1.num_orders()} times at an average price of ${coffee1.average_price():.2f}.")
    print(f"{coffee2.name} has been ordered {coffee2.num_orders()} times at an average price of ${coffee2.average_price():.2f}.")

if _name_ == "_main_":
    run_tests()