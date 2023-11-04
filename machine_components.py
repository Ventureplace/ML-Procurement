# Predefined mapping of machines to their key components
MACHINE_COMPONENTS_MAPPING = {
    "laptop": ["processor", "RAM", "hard drive", "screen", "keyboard", "battery"],
    "smartphone": ["processor", "RAM", "storage", "screen", "battery", "camera"],
    "reactor": ["hopper", "temp gauge", "storage", "mini compressor", "car battery", "camera"]
    # ... add other machines and their components ...
}

def get_components(machine_name):
    """
    Returns the key components of the given machine based on predefined mappings.
    If the machine is not found, returns an empty list.
    """
    return MACHINE_COMPONENTS_MAPPING.get(machine_name.lower(), [])
