import json

models_list = []
with open(r".\ModelsLeaderboard\ModelsLeaderboard\Trending-Models.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        models_list.append(json.loads(line))

for data in models_list:
    print(data)