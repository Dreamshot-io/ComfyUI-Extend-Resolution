class ResolutionPadding:
    """
    A node that takes width and height as integers and outputs padding values
    
    Class methods
    -------------
    INPUT_TYPES (dict):
        Define the input integer parameters for width and height
        
    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tuple (INT values for padding)
    RETURN_NAMES (`tuple`):
        The name of each output (left, top, right, bottom)
    FUNCTION (`str`):
        The name of the entry-point method
    CATEGORY (`str`):
        The category the node appears in
    """
    
    def __init__(self):
        pass
        
    @classmethod
    def INPUT_TYPES(s):
        """
        Define the input fields for width and height as integers
        """
        return {
            "required": {
                "width": ("INT", {
                    "default": 250, 
                    "min": 1,
                    "max": 10000,
                    "step": 1,
                    "display": "number"
                }),
                "height": ("INT", {
                    "default": 250, 
                    "min": 1,
                    "max": 10000,
                    "step": 1,
                    "display": "number"
                }),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "INT", "INT")
    RETURN_NAMES = ("left", "top", "right", "bottom")
    
    FUNCTION = "calculate_padding"
    
    CATEGORY = "Resolution"
    
    def calculate_padding(self, width, height):
        """
        Calculate padding values based on width and height
        
        Parameters:
        width (int): Width of the resolution
        height (int): Height of the resolution
        
        Returns:
        tuple: (left, top, right, bottom) padding values
        """
        # Create the resolution key in the format "widthxheight"
        resolution = f"{width}x{height}"
        
        # Padding values based on the table
        padding_map = {
            "250x250": (0, 0, 0, 0),
            "300x50": (2560, 0, 2560, 0),
            "300x250": (102, 0, 103, 0),
            "300x300": (0, 0, 0, 0),
            "300x600": (0, 512, 0, 512),
            "336x280": (102, 0, 103, 0),
            "970x90": (5006, 0, 5006, 0),
            "980x90": (5063, 0, 5063, 0)
        }
        
        # Return the padding values if the resolution is in our map
        if resolution in padding_map:
            return padding_map[resolution]
        else:
            # Default to zero padding if resolution not found
            print(f"Resolution '{resolution}' not found in padding map. Using zero padding.")
            return (0, 0, 0, 0)


# Add the node to the global node registry
NODE_CLASS_MAPPINGS = {
    "ResolutionPadding": ResolutionPadding
}

# Provide a user-friendly display name
NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionPadding": "Resolution Padding"
}
