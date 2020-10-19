import unittest


def add(x, y):
    return x + y

class ADDTEst(unittest.TestCase):

    def setUp(self):
        #Arrange
        print("SetUp called...")
        self.x = 10
        self.y = -20

    def tearDown(self):
        print("TearDown called...")    
        self.x = 0
        self.y = 0


        
    def test_add_1(self):
        print("Test1 called...")
        #Act
        result = add(self.x,self.y)
        #Assert
        self.assertEqual(result, self.x + self.y)
    

    def test_add_2(self):
        print("Test2 called...")
        #Act
        result = add(self.y,self.x)
        #Assert
        self.assertEqual(result,self.y + self.x)







if __name__ == "__main__":
    unittest.main()