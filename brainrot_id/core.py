import json
import random
import uuid
import hashlib
import time
import os
from pathlib import Path
from typing import Dict, List

class BrainRotGenerator:
    def __init__(self):
        self.phrases = self._load_data('phrases.json')
        self.components = self._load_data('components.json')
        self.transform_history = []

    def _load_data(self, filename: str) -> Dict:
        try:
            from importlib.resources import files
            data = files('brainrot_id.data').joinpath(filename).read_text()
            return json.loads(data)
        except Exception as e:
            raise RuntimeError(f"Failed to load data: {str(e)}")

    def _generate_hash_salt(self) -> str:
        return hashlib.sha3_256(
            f"{uuid.uuid4()}{time.time_ns()}".encode()
        ).hexdigest()[:8]

    def _apply_transform(self, text: str, level: int) -> str:
        transforms = [
            lambda s: s.upper() if random.random() > 0.7 else s,
            lambda s: s + random.choice(['!', '?', '!!']),
            lambda s: s.replace('a', '4').replace('e', '3'),
            lambda s: ' '.join([word * random.randint(1,3) for word in s.split()]),
            lambda s: s + random.choice(self.components['emojis'])
        ]
        for _ in range(level):
            transform = random.choice(transforms)
            text = transform(text)
            self.transform_history.append(transform.__name__)
        return text

    def generate(self, mode: str = 'normal') -> str:
        components = {
            'phrase': random.choice(self.phrases['phrases']),
            'noun': random.choice(self.components['nouns']),
            'verb': random.choice(self.components['verbs']),
            'emoji': random.choice(self.components['emojis'])
        }

        templates = {
            'normal': "{phrase} {noun}-{verb}",
            'extreme': "{noun}{emoji} {phrase} {verb}-XTREME",
            'nuclear': "{phrase} {verb} {noun} {emoji} ::{hash}"
        }

        template = templates.get(mode, templates['normal'])
        result = template.format(
            **components,
            hash=self._generate_hash_salt()
        )
        return self._apply_transform(result, level=3 if mode == 'nuclear' else 1)