from collections import defaultdict


def solution(genres, plays):
    answer = []
    dic_gen = defaultdict(int)
    for g, p in zip(genres, plays):
        dic_gen[g] += p
    dic_gen = sorted(dic_gen.items(), key=lambda x: x[1], reverse=True)
    print(dic_gen)

    dic_pl = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        dic_pl[g].append((p, i))

    for gen, cnt in dic_gen:
        tmp = sorted(dic_pl[gen], key=lambda x: x[0], reverse=True)
        if len(tmp) >= 2:
            answer.append(tmp[0][1])
            answer.append(tmp[1][1])
        elif len(tmp) == 1:
            answer.append(tmp[0][1])


    return answer


'''
from collections import defaultdict
from operator import itemgetter

def solution(genres, plays):
    genre_play_dict = defaultdict(lambda: 0)
    for genre, play in zip(genres, plays):
        genre_play_dict[genre] += play

    genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=itemgetter(1), reverse=True)]
    print(genre_rank)

    final_dict = defaultdict(lambda: [])
    for i, genre_play_tuple in enumerate(zip(genres, plays)):
        final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))
    print(final_dict)

    answer = []
    for genre in genre_rank:
        one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)

        if len(one_genre_list) > 1:
            answer.append(one_genre_list[0][1])
            answer.append(one_genre_list[1][1])
        else:
            answer.append(one_genre_list[0][1])

    print(answer)

    return answer
'''

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])