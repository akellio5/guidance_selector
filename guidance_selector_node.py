class GuidanceSelectorNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "guidance_value": ("FLOAT", {
                    "default": 100.0,
                    "min": 0.0,
                    "max": 100.0,
                    "step": 0.1
                }),
            }
        }

    RETURN_TYPES = ("FLOAT", "BOOLEAN",) 
    FUNCTION = "calculate_guidance"
    CATEGORY = "Custom Nodes/Guidance"

    def calculate_guidance(self, guidance_value):
        value = max(0.0, min(100.0, guidance_value))
        
        # Сегменты для интерполяции (x_high, y_high, x_low, y_low)
        segments = [
            (50.0, 1.5, 40.0, 1.7),
            (40.0, 1.7, 10.0, 1.9),
            (10.0, 1.9, 5.5, 2.2),
            (5.5, 2.2, 4.0, 3.2),
            (4.0, 3.2, 2.0, 3.7),
        ]

        if value >= 50.0:
            output_float = 1.5
        elif value < 2.0:
            output_float = 5.0
        else:
            for x_high, y_high, x_low, y_low in segments:
                if x_low <= value < x_high:
                    slope = (y_low - y_high) / (x_low - x_high)
                    output_float = y_high + slope * (value - x_high)
                    break
            output_float = round(output_float, 1)

        output_bool = value < 4.0

        return (output_float, output_bool,)

NODE_CLASS_MAPPINGS = {"GuidanceSelector": GuidanceSelectorNode}
NODE_DISPLAY_NAME_MAPPINGS = {"GuidanceSelector": "Guidance Selector"}