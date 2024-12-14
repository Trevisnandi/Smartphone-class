class Device:
    """
    A base class representing a generic device.
    """
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        return f"The {self.brand} {self.model} is now powered on."

    def power_off(self):
        return f"The {self.brand} {self.model} is now powered off."

class Smartphone(Device):
    """
    A class representing a smartphone, inheriting from Device.
    """
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)  # Initialize attributes from the parent class
        self.storage = storage
        self.camera_megapixels = camera_megapixels

    def take_picture(self):
        return f"Taking a picture with the {self.camera_megapixels}-megapixel camera."

    def install_app(self, app_name):
        return f"Installing {app_name} on the {self.brand} {self.model}."

    def get_info(self):
        return (
            f"Smartphone Info:\nBrand: {self.brand}\nModel: {self.model}\nStorage: {self.storage} GB\n"
            f"Camera: {self.camera_megapixels} MP"
        )

# Example usage
if __name__ == "__main__":
    my_phone = Smartphone(brand="TechCo", model="XPro Max", storage=256, camera_megapixels=108)

    print(my_phone.power_on())
    print(my_phone.get_info())
    print(my_phone.take_picture())
    print(my_phone.install_app("PLP"))
    print(my_phone.power_off())
