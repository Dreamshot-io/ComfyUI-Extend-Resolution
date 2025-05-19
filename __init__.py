class ResolutionPadding:
    """
    Nodo que toma width/height actuales y deseados (y opcionalmente shrink),
    y devuelve (left, top, right, bottom) de padding para que, al hacer
    resize(desired_width, desired_height), la imagen no se distorsione.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "width":         ("INT", {"default": 250, "min": 1,    "max": 20000, "step": 1}),
                "height":        ("INT", {"default": 250, "min": 1,    "max": 20000, "step": 1}),
                "desired_width": ("INT", {"default": 300, "min": 1,    "max": 20000, "step": 1}),
                "desired_height":("INT", {"default": 300, "min": 1,    "max": 20000, "step": 1}),
                "shrink":        ("BOOLEAN",{"default": False, "display": "checkbox"}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT")
    RETURN_NAMES = ("left", "top", "right", "bottom")
    FUNCTION = "calculate_padding"
    CATEGORY = "Resolution"

    def calculate_padding(self, width, height, desired_width, desired_height, shrink):
        # 1) Opcionalmente reducir la imagen original a la mitad
        if shrink:
            width  = max(1, width  // 2)
            height = max(1, height // 2)

        # 2) Calcular el tamaño de “lienzo” ideal en cada eje para mantener el aspect-ratio
        #    canvas_w = desired_width * height / desired_height
        #    canvas_h = width * desired_height / desired_width
        canvas_w = int(round(desired_width  * height / desired_height))
        canvas_h = int(round(width * desired_height / desired_width))

        # 3) Decidir si rellenar horizontal o vertical
        if canvas_w >= width:
            # padding horizontal
            total_pad = canvas_w - width
            pad_left  = total_pad // 2
            pad_right = total_pad - pad_left
            pad_top = pad_bottom = 0
        else:
            # padding vertical
            total_pad = canvas_h - height
            pad_top    = total_pad // 2
            pad_bottom = total_pad - pad_top
            pad_left = pad_right = 0

        return pad_left, pad_top, pad_right, pad_bottom


# Registrar el nodo
NODE_CLASS_MAPPINGS = {
    "ResolutionPadding": ResolutionPadding
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionPadding": "Resolution Padding"
}
