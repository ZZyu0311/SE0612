
class IconFamily:
    def get_node_icon(self):
        raise NotImplementedError

    def get_leaf_icon(self):
        raise NotImplementedError

class PokerIcons(IconFamily):
    def getNodeIcon(self):
        return "♢"

    def getLeafIcon(self):
        return "♤"

class OtherIcons(IconFamily):
    def getNodeIcon(self):
        return "★"

    def getLeafIcon(self):
        return "☆"