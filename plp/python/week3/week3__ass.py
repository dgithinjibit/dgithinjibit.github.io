"""
A simple script to calculate a final price after a potential discount.
"""

MINIMUM_DISCOUNT_THRESHOLD = 20.0

def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculates the final price after applying a discount.

    The discount is only applied if the discount percentage is 20% or greater.

    Args:
        price: The original price of the item.
        discount_percent: The discount percentage to apply.

    Returns:
        The final price after the discount, or the original price if the
        discount percentage is below the threshold.
    """
    if discount_percent >= MINIMUM_DISCOUNT_THRESHOLD:
        # Simplified calculation for the final price
        return price * (1 - discount_percent / 100)
    else:
        return price

def main():
    """Main function to run the price calculation program."""
    try:
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))

        if price < 0 or discount_percent < 0:
            print("Error: Price and discount percentage cannot be negative.")
            return

        final_price = calculate_discount(price, discount_percent)
        print(f"The final price after applying the discount is: ${final_price:.2f}")

    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")

if __name__ == "__main__":
    main()