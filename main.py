import argparse
from explorer import JSONExplorer
from style import get_style
from icons import get_icon_family

def parse_arguments():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', type=str, required=True, choices=['tree', 'rect'], help='Visualization style (tree or rect)')
    parser.add_argument('-i', '--icon', type=str, required=True, choices=['poker', 'other'], help='Icon family (poker or other)')
    return parser.parse_args()

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_style(style_name):
    if style_name == 'tree':
        return TreeStyle()
    elif style_name == 'rect':
        return RectStyle()
    else:
        raise ValueError(f"Unknown style: {style_name}")

def get_icon_family(icon_name):
    if icon_name == 'poker':
        return PokerIcons()
    elif icon_name == 'other':
        return OtherIcons()
    else:
        raise ValueError(f"Unknown icon family: {icon_name}")

# Ö÷³ÌÐò
def main():
    args = parse_arguments()
    json_data = load_json(args.file)
    style = get_style(args.style)
    icon_family = get_icon_family(args.icon)

    explorer = JSONExplorer(style, icon_family)
    print(explorer.render(json_data))

if __name__ == "__main__":
    main()
