"""Day 02"""


def strip_split_text(path):
    with open(path, "r") as file:
        lines = [line.strip().split(" ") for line in file]
        return lines


def score_round_points(p1_item, p2_item):
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


def fixed_outcome(p1_item, p2_code):
    """
    P2 Codes:
    Z = Win
    Y = Draw
    X = Lose
    """

    fixed_outcomes = {
        "Z": {"rock": "paper", "paper": "scissors", "scissors": "rock"},
        "X": {"rock": "scissors", "scissors": "paper", "paper": "rock"},
    }

    return p1_item if p2_code == "Y" else fixed_outcomes[p2_code][p1_item]


def player_2_fixed_item(p2_code):
    p2_items = {"X": "rock", "Y": "paper", "Z": "scissors"}
    return p2_items[p2_code]


def player_2_item(p1_item, p2_code, fixed_result=False):
    if fixed_result:
        return fixed_outcome(p1_item, p2_code)
    else:
        return player_2_fixed_item(p2_code)


def round_outcome(str_ary, fixed_result=False):
    item_scores = {"rock": 1, "paper": 2, "scissors": 3}
    p1_items = {"A": "rock", "B": "paper", "C": "scissors"}

    p1_code = str_ary[0]
    p1_item = p1_items[p1_code]

    p2_code = str_ary[1]
    p2_item = player_2_item(p1_item, p2_code, fixed_result)

    p1_item_score = item_scores[p1_item]
    p2_item_score = item_scores[p2_item]

    scores = score_round_points(p1_item, p2_item)
    p1_round_score = scores["p1_score"]
    p2_round_score = scores["p2_score"]

    result = {
        "p1": [p1_item_score, p1_round_score],
        "p2": [p2_item_score, p2_round_score],
    }
    return result


def item_and_round_scores(str_ary_ary, fixed_result=False):
    results = {"p1": [], "p2": []}
    for str_ary in str_ary_ary:
        ro = round_outcome(str_ary, fixed_result)
        results["p1"].append(ro["p1"])
        results["p2"].append(ro["p2"])

    return results


def score_sums(iars):
    p1_scores = iars["p1"]
    p2_scores = iars["p2"]

    p1_sums = list(map(lambda ary: sum(ary), p1_scores))
    p2_sums = list(map(lambda ary: sum(ary), p2_scores))

    result = {"p1": p1_sums, "p2": p2_sums}
    return result


def final_scores(path, fixed_result=False):
    str_ary_ary = strip_split_text(path)
    iars = item_and_round_scores(str_ary_ary, fixed_result)
    ss = score_sums(iars)
    final_scores = {"p1": sum(ss["p1"]), "p2": sum(ss["p2"])}
    return final_scores
