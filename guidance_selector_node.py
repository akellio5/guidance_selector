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

    RETURN_TYPES = ("FLOAT", "BOOLEAN", "FLOAT",)
    FUNCTION = "calculate_guidance"
    CATEGORY = "Custom Nodes/Guidance"

    def calculate_output(self, input_value):
        if input_value < 0.5:
            return 5.0
        elif 0.5 <= input_value < 5:
            upper, lower = 5, 0.5
            out_start, out_end = 3.2, 5.0
        elif 5 <= input_value < 10:
            upper, lower = 10, 5
            out_start, out_end = 2.2, 3.2
        elif 10 <= input_value < 40:
            upper, lower = 40, 10
            out_start, out_end = 1.9, 2.2
        elif 40 <= input_value < 50:
            upper, lower = 50, 40
            out_start, out_end = 1.7, 1.9
        elif 50 <= input_value <= 100:
            upper, lower = 100, 50
            out_start, out_end = 1.5, 1.7
        else:
            return None
        
        output = out_start + (upper - input_value) * (out_end - out_start) / (upper - lower)
        return round(output, 1)

    def calculate_denoise(self, input_value):
        input_value = max(0.0, min(100.0, input_value))
        if 40 <= input_value <= 100:
            return 0.0
        elif 10 <= input_value < 40:
            denoise = (40 - input_value) * 0.1 / 30
            return round(denoise, 2)
        elif 0 <= input_value < 10:
            denoise = 0.1 + (10 - input_value) * 0.5 / 10
            return round(denoise, 2)
        else:
            return 0.0

    def calculate_guidance(self, guidance_value):
        value = max(0.0, min(100.0, guidance_value))
        
        output_float = self.calculate_output(value)
        output_bool = value < 4.0
        denoise_value = self.calculate_denoise(value)

        return (output_float, output_bool, denoise_value,)

NODE_CLASS_MAPPINGS = {"GuidanceSelector": GuidanceSelectorNode}
NODE_DISPLAY_NAME_MAPPINGS = {"GuidanceSelector": "Guidance Selector"}