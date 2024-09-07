from math import log10


# Idea: Use bellman for algo to detect negative cycle
# profit if rate_Gold->$ * rate_$->Gold > 1
# for bellman-ford we switch this as it uses additions, so take log
# log(rate_Gold->$ * rate_$->Gold) = log(rate_Gold->$) + log(rate_$->Gold)
# now we can use bellman-ford to see id a loop of transaction can receive endless rewards
# we convert out log's to negative log's
# -log(rate_Gold->$ * rate_$->Gold) = -log(rate_Gold->$) + (-log(rate_$->Gold))
# now if -log(rate_Gold->$) - log(rate_$->Gold) < 0 Then a negative cycle detected
# there is possibility of arbitrage.
def arbitrage(exchange_rates):
    exchange_rates = [[-log10(edge) for edge in row] for row in exchange_rates]
    print(exchange_rates)

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    source = 0
    n = len(exchange_rates)
    min_dist = [float('inf')] * n

    min_dist[source] = 0

    # Relax edges |V - 1| times
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + exchange_rates[v][w]:
                    min_dist[w] = min_dist[v] + exchange_rates[v][w]

    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + exchange_rates[v][w]:
                return True

    return False


if __name__ == '__main__':
    #                gold | $  | Pound
    exchange_rates = [[1, 0.66, 0.77],  # Gold
                      [1.53, 1, 1.16],  # $
                      [1.30, 0.86, 1]]  # Pound


    print('Possible arbitrage: '+ str(arbitrage(exchange_rates)))