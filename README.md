# Design-PatternPython
Using Factory pattern in Food App like Swiggy
the factory pattern to create a food ordering app in Python that functions like Zomato:

I needed to first define an abstract Restaurant class with get_menu() and place_order() methods. 

I then implement concrete restaurant classes like PizzaRestaurant and SushiRestaurant that inherit from Restaurant and provide their own menu and order placement logic.

The RestaurantFactory class serves as the factory, which creates instances of the concrete restaurant classes based on the given restaurant type.

In the main() function,this part shows the usage of the factory pattern by creating a pizza restaurant and a sushi restaurant using the RestaurantFactory and placing orders with different items at each restaurant.

Note: This example is a simplified version and may not cover all the functionalities of a complete food ordering app like Zomato, but it provides a basic structure to demonstrate the factory pattern in Python.
