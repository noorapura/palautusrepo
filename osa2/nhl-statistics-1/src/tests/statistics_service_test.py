import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_fail(self):
	    haku = self.stats.search("noora")
	    self.assertIsNone(haku)

    def test_search(self):
	    pelaaja = self.stats.search("Kurri")
	    print(pelaaja)  
	    oikea = Player("Kurri", "EDM", 37, 53)
	    self.assertAlmostEqual(print(pelaaja), print(oikea))

    
    def test_team(self):
	    haku = self.stats.team("PIT")
	    self.assertAlmostEqual(haku[0].name, "Lemieux")


    def test_top(self):
	    haku = self.stats.top(2)
	    self.assertAlmostEqual(haku[0].name, "Gretzky")
	    self.assertAlmostEqual(haku[1].name, "Lemieux")	
