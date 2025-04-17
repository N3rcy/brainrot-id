from .core import BrainRotGenerator
from .cli import main

__version__ = "0.1.0"
__all__ = ['BrainRotGenerator', 'generate_id']

def generate_id(mode: str = 'normal') -> str:
    return BrainRotGenerator().generate(mode)