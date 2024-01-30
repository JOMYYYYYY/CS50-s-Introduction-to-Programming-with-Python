
   # Resin sale helper
#### Video Demo:  <https://youtu.be/e3LOB48Hc_4>
#### Description:

The software will help sales to sell the products which are three (or much more) kinds of resins that is used for water purification. When the user input the name of the resin, the user can get some basic information. For example, the price of the resin per liter, the strength of the resin and some case projects.

The user will be asked to input basic information about the current water purification project that need to use at least one of the resin products.

The basic information is simplified into three parts which are the volume of the polluted water per hour, the concentrations of the pollutants in the incoming polluted water as will as the required concentrations of the pollutants in processed clean water, the last is the type of the pollutant.

After the user input the name of the resin and the basic project information, the software will automatically count the total amount of the cost and the mount of the resin usage, by which the project will be marked as a "A/B/C"  project. According to the level of the projects the suggestions given to the sales are different.

The following content will explain some code details:

First, we make a class called Resin, which has 6 features:

"name" is the specific type of the resin product

"price" is the value or cost of money of the specific resin per liter

"pollutant" is the type of source material that cause pollution

"capacity" is the adsorption capacity of corresponding  pollutant per liter

"strength" is the brief introduction of the advantage of the specific type of resin

"case_projects" are successful projects implemented the specific type of resin

For now, there are only 3 types of the resin products available, which are T-42, CH-90, A-62. Each of them have accordingly different other features. Once the user input the name of the resin, the other feature will be automatically set up by the object oriented programming set.

There are only three functions in this project: count_usage_amount, count_price, suggestion. You can guess the usages of the functions by their names. Based on the user input information(the volume of the polluted water per hour, the concentrations of the pollutants in the incoming polluted water as will as the required concentrations of the pollutants in processed clean water, the last is the type of the pollutant), the function will work out and give the user information including the total price and amount, the project classification, based on which the suggestion will be given to user as well.

That's it!

