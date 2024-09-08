from src.creation.builder.factory.build_margherita import MargheritaPizzaBuilder
from src.creation.builder.factory.build_pepperon import PepperoniPizzaBuilder
from src.creation.builder.process.pizza_direct import PizzaDirector
from src.utils.logger import logger

if __name__ == "__main__":
    margherita_builder = MargheritaPizzaBuilder()
    pepperoni_builder = PepperoniPizzaBuilder()

    margherita = PizzaDirector(margherita_builder).make_pizza()
    logger.info(repr(margherita))

    pepperoni = PizzaDirector(pepperoni_builder).make_pizza()
    logger.info(repr(pepperoni))
