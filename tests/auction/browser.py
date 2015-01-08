import unittest

import pydarkstar.logutils
import pydarkstar.database
import pydarkstar.auction.browser
import pydarkstar.rc
import logging

pydarkstar.logutils.setDebug()

class TestCase(unittest.TestCase):
    def setUp(self):
        self.db = pydarkstar.database.Database.pymysql(**pydarkstar.rc.sql)
        self.ob = pydarkstar.auction.browser.Browser(self.db, fail=True)

    def test_init(self):
        pass

    def test_count(self):
        self.ob.count()

    def test_getStock(self):
        logging.debug('stock = %s', self.ob.getStock(1, 0))

    def test_getPrice(self):
        logging.debug('price = %s', self.ob.getPrice(1, 0))

if __name__ == '__main__':
    unittest.main()