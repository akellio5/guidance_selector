from .guidance_selector_node import GuidanceSelectorNode

NODE_CLASS_MAPPINGS = {
    "GuidanceSelector": GuidanceSelectorNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GuidanceSelector": "Guidance Selector"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']