# Define the abstract class for the restaurant
class Restaurant:
    def get_menu(self):
        pass

    def place_order(self, items):
        pass


# Concrete implementation of the restaurant class
class PizzaRestaurant(Restaurant):
    def get_menu(self):
        return {
            'Margherita': 10,
            'Pepperoni': 12,
            'Veggie Supreme': 13
        }

    def place_order(self, items):
        total_cost = sum(self.get_menu().get(item, 0) for item in items)
        print(f"Placing order for {', '.join(items)} from Pizza Restaurant. Total cost: {total_cost}")


class SushiRestaurant(Restaurant):
    def get_menu(self):
        return {
            'California Roll': 8,
            'Salmon Nigiri': 10,
            'Tempura': 15
        }

    def place_order(self, items):
        total_cost = sum(self.get_menu().get(item, 0) for item in items)
        print(f"Placing order for {', '.join(items)} from Sushi Restaurant. Total cost: {total_cost}")


# Factory class to create restaurants
class RestaurantFactory:
    @staticmethod
    def create_restaurant(restaurant_type):
        if restaurant_type == 'Pizza':
            return PizzaRestaurant()
        elif restaurant_type == 'Sushi':
            return SushiRestaurant()
        else:
            raise ValueError("Invalid restaurant type.")


# Client code
def main():
    # Create a pizza restaurant
    pizza_restaurant = RestaurantFactory.create_restaurant('Pizza')
    menu = pizza_restaurant.get_menu()
    print("Pizza Restaurant Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

    # Place an order at the pizza restaurant
    items = ['Margherita', 'Pepperoni']
    pizza_restaurant.place_order(items)

    print()

    # Create a sushi restaurant
    sushi_restaurant = RestaurantFactory.create_restaurant('Sushi')
    menu = sushi_restaurant.get_menu()
    print("Sushi Restaurant Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

    # Place an order at the sushi restaurant
    items = ['California Roll', 'Tempura']
    sushi_restaurant.place_order(items)


if __name__ == '__main__':
    main()

