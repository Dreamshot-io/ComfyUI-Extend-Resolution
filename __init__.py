class ResolutionPadding:
    """
    A node that takes a target resolution string and outputs padding values
    
    Class methods
    -------------
    INPUT_TYPES (dict):
        Define the input string parameter for resolution
        
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
        Define the input field for the resolution string
        """
        return {
            "required": {
                "target_resolution": ("STRING", {
                    "multiline": False,
                    "default": "250x250"
                }),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "INT", "INT")
    RETURN_NAMES = ("left", "top", "right", "bottom")
    
    FUNCTION = "calculate_padding"
    
    CATEGORY = "Resolution"
    
    def calculate_padding(self, target_resolution):
        """
        Calculate padding values based on the target resolution string
        
        Parameters:
        target_resolution (str): Resolution in format "widthxheight"
        
        Returns:
        tuple: (left, top, right, bottom) padding values
        """
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
        
        # Normalize the resolution string (trim spaces, ensure lowercase)
        resolution = target_resolution.strip().lower()
        
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