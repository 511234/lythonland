from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    # 知道要起個payload出黎，唔知實際點起
    def make_payload_method(self):
        pass

    # Create product & output (too much?)
    def build_payload(self) -> str:
        product: Product = self.make_payload_method()
        result = f"Creator: The same creator's code has just worked with {product.display_output()}"

        return result


class CreateProductPayloadCreator(Creator):
    def __init__(self, source, *args, **kwargs):
        self.source = source

    def make_payload_method(self) -> Product:
        return CreateProductPayload()


class UpdateProductPayloadCreator(Creator):
    def __init__(self, source, *args, **kwargs):
        self.source = source

    def make_payload_method(self) -> Product:
        return UpdateProductPayload()


class UpsertSpecPayloadCreator(Creator):
    def __init__(self, source, *args, **kwargs):
        self.source = source

    def make_payload_method(self) -> Product:
        return UpsertSpecPayload()


# Similar to interface
class Product(ABC):
    @abstractmethod
    def display_output(self) -> str:
        pass


class CreateProductPayload(Product):
    def display_output(self) -> str:
        return "{Result of the CreateProductPayload}"


class UpdateProductPayload(Product):
    def display_output(self) -> str:
        return "{Result of the UpdateProductPayload}"


class UpsertSpecPayload(Product):
    def display_output(self) -> str:
        return "{Result of the UpsertSpecPayload}"


def client_code(creator: Creator) -> None:
    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.build_payload()}",
        end="",
    )


if __name__ == "__main__":

    source = {
        "name": "a bag of yummy orange",
        "price": 20.0,
        "color": "#FFA500",
        "origin": "New Zealand",
        "quantity": 30,
        "remarks": [
            {
                "company": "Fruity Monday",
                "description": "An orange a day keeps a doctor away",
                "discount": 0.3,
                "hashtag": ["orange", "fruit"],
                "organic": True,
                "promotion_code": "yumyum",
                "promotion_until": "2022-12-31",
                "seller": "Mr. Brown",
            }
        ],
    }

    print("App: Launched with the CreateProductPayloadCreator.")
    client_code(CreateProductPayloadCreator(source))
    print("\n")

    print("App: Launched with the UpdateProductPayloadCreator(Creator):.")
    client_code(UpdateProductPayloadCreator(source))
    print("\n")

    print("App: Launched with the UpsertSpecPayloadCreator(Creator):.")
    client_code(UpsertSpecPayloadCreator(source))
    print("\n")


# client_code > creator.build_payload > make_payload_method > display_output
