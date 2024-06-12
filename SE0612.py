import json
import argparse

class IconKu:
    def getNodeIcon(self):
        raise NotImplementedError

    def getLeafIcon(self):
        raise NotImplementedError

class NiceIcon(IconKu):
    def getNodeIcon(self):
        return "♢"

    def getLeafIcon(self):
        return "♤"

class StarIcon(IconKu):
    def getNodeIcon(self):
        return "★"

    def getLeafIcon(self):
        return "☆"


class Style:
    def render(self, json_data, icons):
        raise NotImplementedError

class TreeStyle(Style):
    def render(self, json_data, icons):
        return self._render_node(json_data, 0, icons)

    def _render_node(self, node, level, icons):
        result = ""
        indent = "│  " * level
        for key, value in node.items():
            if isinstance(value, dict):
                result += f"{indent}├─{icons.getNodeIcon()}{key}\n"
                result += self._render_node(value, level + 1, icons)
            else:
                result += f"{indent}└─{icons.getLeafIcon()}{key}: {value}\n"
        return result

class RectangleStyle(Style):
    def render(self, json_data, icons):
        return self._render_node(json_data, 0, icons)

    def _render_node(self, node, level, icons):
        result = ""
        indent = "│  " * level
        for key, value in node.items():
            if isinstance(value, dict):
                result += f"{indent}├─{icons.getNodeIcon()}{key}─" + "─" * 30 + "┐\n"
                result += self._render_node(value, level + 1, icons)
            else:
                result += f"{indent}└─{icons.getLeafIcon()}{key}: {value}─" + "─" * 30 + "┤\n"
        return result

def parse_arguments():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', type=str, required=True, choices=['tree', 'rectangle'], help='tree or rectangle')
    parser.add_argument('-i', '--icon', type=str, required=True, choices=['nice', 'star'], help='nice or star')
    return parser.parse_args()

def get_jsonfile(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_style(style_name):
    if style_name == 'tree':
        return TreeStyle()
    elif style_name == 'rectangle':
        return RectangleStyle()
    else:
        raise ValueError(f"Unknown style: {style_name}")

def get_icon(icon_name):
    if icon_name == 'nice':
        return NiceIcon()
    elif icon_name == 'star':
        return StarIcon()
    else:
        raise ValueError(f"Unknown icon: {icon_name}")

class JSONExplorer:
    def __init__(self, style, icon_family):
        self.style = style
        self.icon_family = icon_family

    def render(self, json_data):
        return self.style.render(json_data, self.icon_family)
        
def main():
    args = parse_arguments()
    json_data = get_jsonfile(args.file)
    style = get_style(args.style)
    icon_family = get_icon(args.icon)

    explorer = JSONExplorer(style, icon_family)
    print(explorer.render(json_data))

if __name__ == "__main__":
    main()

