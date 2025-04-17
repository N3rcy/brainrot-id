from brainrot_id import BrainRotGenerator
import re

def test_generation():
    generator = BrainRotGenerator()
    id_pattern = re.compile(r"[\w\s!?-]+(::[a-f0-9]{8})?")
    
    for mode in ['normal', 'extreme', 'nuclear']:
        result = generator.generate(mode)
        assert id_pattern.match(result), f"Invalid ID format in mode {mode}"
        assert len(result) >= 10, f"ID too short in mode {mode}"