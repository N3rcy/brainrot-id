import argparse
from .core import BrainRotGenerator

def main():
    parser = argparse.ArgumentParser(
        description='Generate brain-rot IDs for modern applications'
    )
    parser.add_argument(
        '-m', '--mode',
        choices=['normal', 'extreme', 'nuclear'],
        default='normal',
        help='Generation mode'
    )
    parser.add_argument(
        '-c', '--count',
        type=int,
        default=1,
        help='Number of IDs to generate'
    )
    
    args = parser.parse_args()
    generator = BrainRotGenerator()
    
    for _ in range(args.count):
        print(generator.generate(mode=args.mode))

if __name__ == '__main__':
    main()