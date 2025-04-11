from collections import defaultdict


CSV_PATH = "csv/movielist.csv"


def split_producers(producer_str):
    return [p.strip() for p in producer_str.replace(" and ", ",").split(",") if p.strip()]


def get_prize_intervals(rows):
    producer_wins = defaultdict(list)
    for year, producers_str in rows:
        producers = split_producers(producers_str)
        for producer in producers:
            producer_wins[producer].append(year)

    intervals = []
    for producer, years in producer_wins.items():
        years.sort()
        for i in range(1, len(years)):
            interval = years[i] - years[i - 1]
            intervals.append({
                "producer": producer,
                "interval": interval,
                "previousWin": years[i - 1],
                "followingWin": years[i]
            })

    if not intervals:
        return {"min": [], "max": []}

    min_interval = min(i["interval"] for i in intervals)
    max_interval = max(i["interval"] for i in intervals)

    return {
        "min": [i for i in intervals if i["interval"] == min_interval],
        "max": [i for i in intervals if i["interval"] == max_interval]
    }
