import json

with open("./chinese/items.json", "r") as handler:
    characters = json.load(handler)

characters = list(filter(lambda c: c["character"] is not None, characters))
for c in characters:
    if int(c["standard"]) < 3501:
        c["GSCC"] = "Level 1"
    elif int(c["standard"]) < 6501:
        c["GSCC"] = "Level 2"
    else:
        c["GSCC"] = "Level 3"

def group_characters(group_key, additional_level):
    c_to_k = [(c['character'], c[group_key] if c[group_key] is not None else additional_level) for c in characters]
    groups = {}
    for c, k in c_to_k:
        if k in groups.keys():
            groups[k].append(c)
        else:
            groups[k] = [c]
    groups["Out of GSCC"] = []
    return groups


def from_dict_to_KanjiGroup(groups):
    results = []
    for key in groups.keys():
        results.append((key, ''.join(groups[key])))
    return results


hsk_groups = from_dict_to_KanjiGroup(group_characters("hsk_level", "Not in HSK"))
official_frequency_groups = from_dict_to_KanjiGroup(group_characters("GSCC", ""))

print(hsk_groups)
print(official_frequency_groups)
