class Product:
    """
    Represents a product with a name and price.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class ShippingMethod:
    """
    Base class for different shipping methods.
    """
    def calculate_cost(self) -> float:
        raise NotImplementedError("This method should be implemented in subclasses.")

    def estimated_delivery_time(self) -> str:
        raise NotImplementedError("This method should be implemented in subclasses.")

class StandardShipping(ShippingMethod):
    """
    Standard shipping: low cost but slow.
    """
    def calculate_cost(self) -> float:
        return 5.00

    def estimated_delivery_time(self) -> str:
        return "5-7 business days"

class ExpressShipping(ShippingMethod):
    """
    Express shipping: higher cost but fast.
    """
    def calculate_cost(self) -> float:
        return 15.00

    def estimated_delivery_time(self) -> str:
        return "1-2 business days"

class CustomShipping(ShippingMethod):
    """
    Custom shipping: cost varies based on distance.
    """
    def __init__(self, distance: float):
        self.distance = distance

    def calculate_cost(self) -> float:
        return max(10.00, self.distance * 0.50)

    def estimated_delivery_time(self) -> str:
        return f"Estimated {self.distance / 100:.1f} days based on distance"

class Order:
    """
    Represents an order with a product and shipping method.
    """
    def __init__(self, product: Product, shipping: ShippingMethod):
        self.product = product
        self.shipping = shipping

    def total_cost(self) -> float:
        return self.product.price + self.shipping.calculate_cost()

    def order_summary(self) -> str:
        return (f"Order Summary:\nProduct: {self.product}\n"
                f"Shipping Cost: ${self.shipping.calculate_cost():.2f}\n"
                f"Estimated Delivery: {self.shipping.estimated_delivery_time()}\n"
                f"Total Cost: ${self.total_cost():.2f}")

# User interaction
print("Welcome to the purchase and shipping system!")
product_name = input("Enter the product name: ")
product_price = float(input("Enter the product price: "))
product = Product(product_name, product_price)

shipping_methods = {
    "1": StandardShipping(),
    "2": ExpressShipping(),
    "3": lambda: CustomShipping(float(input("Enter distance for custom shipping: ")))
}

print("Select a shipping method:\n1. Standard ($5, 5-7 days)\n2. Express ($15, 1-2 days)\n3. Custom (Varies by distance)")
choice = input("Enter your choice (1, 2, or 3): ")

shipping_method = shipping_methods.get(choice, StandardShipping())
if callable(shipping_method):
    shipping_method = shipping_method()

order = Order(product, shipping_method)
print(order.order_summary())
