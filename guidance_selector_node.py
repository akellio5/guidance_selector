import comfy

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
        

        if value >= 50:
            output_float = 1.5
        elif value >= 40:
            output_float = 1.7
        elif value >= 10:
            output_float = 1.9
        elif value >= 5.5:
            output_float = 2.2
        elif value >= 4:
            output_float = 3.2
        elif value >= 2:
            output_float = 3.7
        else:
            output_float = 5

        output_bool = value < 4.0

        return (output_float, output_bool,)

NODE_CLASS_MAPPINGS = {"GuidanceSelector": GuidanceSelectorNode}
NODE_DISPLAY_NAME_MAPPINGS = {"GuidanceSelector": "Guidance Selector"}