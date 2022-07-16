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
    def make_payload_method(self) -> Product:
        return CreateProductPayload()


class UpdateProductPayloadCreator(Creator):
    def make_payload_method(self) -> Product:
        return UpdateProductPayload()


class UpsertSpecPayloadCreator(Creator):
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
    print("App: Launched with the CreateProductPayloadCreator.")
    client_code(CreateProductPayloadCreator())
    print("\n")

    print("App: Launched with the UpdateProductPayloadCreator(Creator):.")
    client_code(UpdateProductPayloadCreator())
    print("\n")

    print("App: Launched with the UpsertSpecPayloadCreator(Creator):.")
    client_code(UpsertSpecPayloadCreator())
    print("\n")


# client_code > creator.build_payload > make_payload_method > display_output