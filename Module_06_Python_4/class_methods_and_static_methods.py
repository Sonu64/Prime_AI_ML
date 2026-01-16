class SmartPhone:
    brand = "Generic"  # Class Variable

    def __init__(self, model):
        self.model = model

    # 1. CLASS METHOD
    # Takes 'cls' as the first parameter.
    # Use this when you need to access or modify the class state (like class variables).
    @classmethod
    def set_brand(cls, new_brand):
        cls.brand = new_brand
        print(f"All smartphones are now branded as: {cls.brand}")

    # 2. STATIC METHOD
    # Takes no special first parameter (no self, no cls).
    # Use this for "utility" functions that don't need to touch class or instance data.
    @staticmethod
    def is_valid_os(os_name):
        valid_os = ["iOS", "Android", "OxygenOS"]
        return os_name in valid_os

# --- How to use them ---

# Calling Class Method: Changes the 'brand' for the WHOLE class
SmartPhone.set_brand("Titan")

# Calling Static Method: Just a helper function
print(f"Is Windows a phone OS? {SmartPhone.is_valid_os('Windows')}")