# Dictionary and counter in Python to find winner of election


def vote_counter(ballots):
    election = {}
    for item in ballots:
        if item not in election:
            election[ballots.count(item)] = item
    sorted(election)
    winner = list(election.values())
    return {
        'election_result': election,
        'winner': winner[0]
    }


try:
    contestants, votes = [], []
    num_candidates = int(input('Enter the number of contestants : '))
    for index in range(num_candidates):
        while True:
            name = input(f'Enter the {index + 1} candidate\'s name : ')
            if len(name):
                contestants.append(name.lower())
                break
            else:
                print(f'Invalid name for {index + 1} contestant. Try again')
    vote_count = int(input('Enter the number of votes : '))

    for index in range(vote_count):
        vote = input(f'Enter the {index + 1} vote : ')
        if vote.lower() in contestants:
            votes.append(vote.lower())
        else:
            print('Invalid candidate name. Vote cancelled.')

    result = vote_counter(votes)
    print('-'*70)
    print(f'Election winner : {result["winner"]}')
    print('Election Results ')
    for k, v in result['election_result'].items():
        print(f'{v} got {k} votes out of {vote_count} votes')
    if vote_count > len(votes):
        print(f'Number of cancelled votes : '
              f'{vote_count - len(votes)} out of {vote_count} votes')


except ValueError:
    print('Invalid Input')
