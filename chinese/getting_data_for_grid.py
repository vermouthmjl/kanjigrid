import json

with open("./chinese/items.json", "r") as handler:
    characters = json.load(handler)

characters = list(filter(lambda c: c["character"] is not None, characters))
for c in characters:
    c["frequency_group"] = "Common"
    if c["standard"] is None:
        c["GSCC"] = None
    elif int(c["standard"]) < 3501:
        c["GSCC"] = "Level 1"
    elif int(c["standard"]) < 6501:
        c["GSCC"] = "Level 2"
    else:
        c["GSCC"] = "Level 3"

characters.sort(key=lambda c: int(c['frequency_rank']))


def group_characters(group_key, additional_level, sort_by):
    sorted_c = list(filter(lambda c: c[sort_by] is not None, characters))
    sorted_c.sort(key=lambda x: int(x[sort_by]))
    c_to_k = [(c['character'], c[group_key]) for c in sorted_c]
    groups = {additional_level: []}
    for c, k in c_to_k:
        if k is not None:
            if k in groups.keys():
                groups[k].append(c)
            else:
                groups[k] = [c]
    return groups


def from_dict_to_KanjiGroup(groups):
    results = []
    for key in groups.keys():
        results.append((key, ''.join(groups[key])))
    return results


hsk_groups = from_dict_to_KanjiGroup(group_characters("hsk_level", "Not in HSK", "frequency_rank"))
official_frequency_groups = from_dict_to_KanjiGroup(group_characters("GSCC", "Not in GSCC", "standard"))
frequency_groups = from_dict_to_KanjiGroup(group_characters("frequency_group", "Not in common characters", "frequency_rank"))

print(hsk_groups)
print(official_frequency_groups)
print(frequency_groups)
