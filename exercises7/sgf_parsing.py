import re
class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []
    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True
    def __ne__(self, other):
        return not self == other
def parse(input_string):
    section_list = []
    
    if input_string.count("(") == 0 or input_string.count(")") == 0:
        raise ValueError("tree missing")
    section, input_string = get_next_section(input_string)
    if ";" not in section or section.index(";") != 0:
        raise ValueError("tree with no nodes")
    if "(" not in section:
        section_list.append(section)
    while "(" in section:
        if len(section[: section.index("(")]) > 0:
            section_list.append(section[: section.index("(")])
        section, other = get_next_section(section[section.index("("):])
        if "(" not in section:
            section_list.append(section)
            section = other
    subsection_list = get_subsections("".join(section_list))
    root = SgfTree(get_properties(subsection_list.pop(0), {}))
    for sub in subsection_list:
        root.children.append(SgfTree(get_properties(sub, {})))
    return root
def get_next_section(input_string):
    paren_match, count = 0, 0
    for i, c in enumerate(input_string):
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1
            if count == 0:
                paren_match = i
                break
    section = input_string[input_string.index("(") + 1: paren_match]
    return section, input_string[paren_match + 1:]
def get_properties(string, prop_dict):
    key = ""
    str_block = ""
    if "[" in string:
        key = string[: string.index("[")]
        if "\]" in string:
            str_block = string[string.index("\]") + 1: string.rindex("\]")] + "]"
            string = string[: string.index("\]")] + string[string. rindex("\]") + 2:]
    elif len(string) == 0:
        return prop_dict
    else: 
        raise ValueError("properties without delimiter")
    if not key.isupper():
        raise ValueError("property must be in uppercase")
    string = string.replace("][", "")
    start_i, end_i = string.index("["), string.index("]")
    for c in string[start_i + 1: end_i]:
        if key in prop_dict:
            prop_dict[key].append(c)
        else:
            prop_dict[key] = [c]
    if len(str_block) > 0:
        str_block = str_block.replace("\t", " ")
        if key in prop_dict:
            prop_dict[key].append(str_block)
        else:
            prop_dict[key] = [str_block]
    if len(string) == end_i + 1 or string[end_i + 1] == "(":
        return prop_dict
    return get_properties(string[end_i + 1:], prop_dict)
def get_subsections(section):
    semicolon_indices = [i for i, c in enumerate(section) if c == ";"]
    if len(semicolon_indices) == 0:
        semicolon_indices = [0]
    section_list = [section[1 + semicolon_indices[i - 1]: semicolon_indices[i]] for i in range(1, len(semicolon_indices))]
    section_list.append(section[1 + semicolon_indices[-1]:])
    return section_list