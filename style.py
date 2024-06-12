class Style:
    def render(self, json_data, icons):
        raise NotImplementedError

class TreeStyle(Style):
    def render(self, json_data, icons):
        return self._render_node(json_data, 0, icons)

    def _render_node(self, node, level, icons):
        result = ""
        indent = "©¦  " * level
        for key, value in node.items():
            if isinstance(value, dict):
                result += f"{indent}©À©¤{icons.getNodeIcon()}{key}\n"
                result += self._render_node(value, level + 1, icons)
            else:
                result += f"{indent}©¸©¤{icons.getLeafIcon()}{key}: {value}\n"
        return result

class RectStyle(Style):
    def render(self, json_data, icons):
        return self._render_node(json_data, 0, icons)

    def _render_node(self, node, level, icons):
        result = ""
        indent = "©¦  " * level
        for key, value in node.items():
            if isinstance(value, dict):
                result += f"{indent}©À©¤{icons.getNodeIcon()}{key}©¤" + "©¤" * 30 + "©´\n"
                result += self._render_node(value, level + 1, icons)
            else:
                result += f"{indent}©¸©¤{icons.getLeafIcon()}{key}: {value}©¤" + "©¤" * 30 + "©È\n"
        return result
