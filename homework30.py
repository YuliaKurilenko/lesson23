class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        out = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                out[k] = str(v)
            print(out)

    def test_turn1(self):
        turn_1 = Tournament(90, self.runner1, self.runner3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['test_turn1'] = result

    def test_turn2(self):
        turn_2 = Tournament(90, self.runner2, self.runner3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', ' Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    def test_turn3(self):
        turn_3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', ' Последним должен быть Ник')
        self.all_results['test_turn3'] = result

    def test_turn4(self):
        turn_4 = Tournament(20, self.runner1, self.runner2, self.runner3)
        result = turn_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', ' Последним должен быть Ник')
        self.all_results['test_turn4'] = result

    if __name__ == '__main__':
        unittest.main()
