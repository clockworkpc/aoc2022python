"""Day 02"""

import re


def strip_split_text(path):
    with open(path, "r") as file:
        lines = [line.strip().split(" ") for line in file]
        return lines


def scoring_system_old(p1_item, p2_item):
    items = [p1_item, p2_item]

    draw = p1_item == p2_item
    rock_vs_paper = "rock" in items and "paper" in items
    paper_vs_scissors = "paper" in items and "scissors" in items
    scissors_vs_rock = "scissors" in items and "rock" in items

    if draw:
        p1_score = 3
        p2_score = 3
    elif rock_vs_paper:
        p1_score = 0 if p1_item == "rock" else 6
        p2_score = 6 if p1_item == "rock" else 0
    elif paper_vs_scissors:
        p1_score = 0 if p1_item == "paper" else 6
        p2_score = 6 if p1_item == "paper" else 0
    elif scissors_vs_rock:
        p1_score = 0 if p1_item == "scissors" else 6
        p2_score = 6 if p1_item == "scissors" else 0

    result = {"p1_score": p1_score, "p2_score": p2_score}
    return result


def scoring_system_new(p1_item, p2):
    p2_win = p2 == "Z"
    p2_draw = p2 == "Y"
    p2_lose = p2 == "X"

    necessary_results = {
        "p2_win": {"rock": "paper", "paper": "scissors", "scissors": "rock"},
        "p2_lose": {"rock": "scissors", "scissors": "paper", "paper": "rock"},
        "p2_draw": {
            "rock": "rock",
            "paper": "paper",
            "scissors": "scissors",
        },
    }

    if p2_win:
        p2_item = necessary_results["p2_win"][p1_item]
        p2_item = necessary_results["p2_win"][p1_item]
    elif p2_lose:
        p2_item = necessary_results["p2_lose"][p1_item]
    elif p2_draw:
        p2_item = p1_item

    print(f"P1 ITEM: {p1_item}")
    print(f"LETTER: {p2}")
    print(f"P2 ITEM: {p2_item}")
    return scoring_system_old(p1_item, p2_item)


def round_results(str_ary, new_scoring_system=False):
    p1 = str_ary[0]
    p2 = str_ary[1]

    p1_items = {"A": "rock", "B": "paper", "C": "scissors"}
    p2_items = {"X": "rock", "Y": "paper", "Z": "scissors"}
    item_scores = {"rock": 1, "paper": 2, "scissors": 3}

    p1_item = p1_items[p1]
    p2_item = p2_items[p2]

    p1_item_score = item_scores[p1_item]
    p2_item_score = item_scores[p2_item]
    round_items = [p1_item, p2_item]

    if new_scoring_system:
        print("NEW SCORING SYSTEM")
        scores = scoring_system_new(p1_item, p2)
    else:
        scores = scoring_system_old(p1_item, p2_item)

    p1_round_score = scores["p1_score"]
    p2_round_score = scores["p2_score"]

    result = {
        "p1": [p1_item_score, p1_round_score],
        "p2": [p2_item_score, p2_round_score],
    }
    print(f"ROUND RESULT: {result}")
    return result


def item_and_round_scores(str_ary_ary, new_scoring_system=False):
    results = {"p1": [], "p2": []}
    for str_ary in str_ary_ary:
        rr = round_results(str_ary, new_scoring_system)
        results["p1"].append(rr["p1"])
        results["p2"].append(rr["p2"])

    return results


def score_sums(item_and_round_scores):
    p1_scores = item_and_round_scores["p1"]
    p2_scores = item_and_round_scores["p2"]

    p1_sums = list(map(lambda ary: sum(ary), p1_scores))
    p2_sums = list(map(lambda ary: sum(ary), p2_scores))

    result = {"p1": p1_sums, "p2": p2_sums}
    return result


def final_scores(path, new_scoring_system=False):
    str_ary_ary = strip_split_text(path)
    iars = item_and_round_scores(str_ary_ary, new_scoring_system)
    ss = score_sums(iars)
    final_scores = {"p1": sum(ss["p1"]), "p2": sum(ss["p2"])}
    return final_scores
