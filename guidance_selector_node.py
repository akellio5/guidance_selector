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

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "calculate_guidance"
    CATEGORY = "Custom Nodes/Guidance"

    def calculate_guidance(self, guidance_value):
        value = max(0.0, min(100.0, guidance_value))
        if value >= 50:
            output = 1.5
        elif value >= 40:
            output = 1.8
        elif value >= 10:
            output = 2.0
        elif value >= 5.5:
            output = 2.3
        elif value >= 4:
            output = 2.8
        else:
            output = 2.9
        return (output,)