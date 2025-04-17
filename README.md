# 🧠💢 BrainRot-ID

**BrainRot-ID** is a post-modern, meme-fueled ID generator for:
- Meme-based systems
- Absurdist programming
- Cryptography experiments
- Anyone bored with UUIDs

## 🚀 Features

- **Three generation modes:** `normal`, `extreme`, `nuclear`
- **Built-in meme dictionary** (absurdist, Italian-sounding words)
- **Cryptographic uniqueness** (SHA3-256 + UUID)
- **Emoji integration** for extra flair
- **Random transformations:** upper-case, character swaps, repetitions, emoji, and more
- **CLI & Python API**
- **Easily extendable** — add your own phrases!

## 🛠️ Installation

```bash
pip install brainrot-id
```

## 🐍 Usage in Python

```python
from brainrot_id import generate_id

print(generate_id('nuclear'))
# Example output: "TUNGx6 SAHUR💥 ::deadbeef"
```

Available modes: `'normal'`, `'extreme'`, `'nuclear'`.

## 💻 Command Line Usage

```bash
brainrot-id --mode nuclear --count 3
```

- `--mode` — generation mode (`normal`, `extreme`, `nuclear`)
- `--count` — number of IDs to generate

## 🧩 How does it work?

The generator randomly combines meme phrases, Italian-style nouns and verbs, emojis, and a cryptographic hash. In `nuclear` mode, extra random transformations are applied for maximum chaos.

## 🧪 Testing

Basic tests ensure ID format and length for all modes:

```bash
pytest tests/
```

## 🤝 Contributing

PRs with new meme phrases or ideas are welcome! Just add them to `data/phrases.json` or `data/components.json`.

## 📄 License

MIT