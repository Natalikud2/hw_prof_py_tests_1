import unittest
from main import people,add_doc,delete,documents,directories
from parameterized import parameterized


class TestFunctions(unittest.TestCase):
#тест функции поиска владельца по номеру документа
    @parameterized.expand(
        [("10006",'Аристарх Павлов'),
         ("10007",None)]
    )
    def test_people(self,number_input,result):
        testresult = people(number_input)
        self.assertEqual(testresult,result)

#тест функции добавления документа на полку add_doc
    @parameterized.expand(
        [('some','some','some','3','success'),
         ('some','some','some','4','shelf not found')]
    )
    def test_add_doc(self,type_input,number_input,name_input,shelf_input,result):

        testresult = add_doc(type_input,number_input,name_input,shelf_input)
        self.assertEqual(testresult,result)


#тест функции удаления документа delete
    @parameterized.expand(
        [('2207 876234','success deleted from documents and directories'),
         ('3232','not found')]
    )
    def test_delete(self,number_input,result):

        testresult = delete(number_input)
        self.assertEqual(testresult,result)

if __name__=='__main__':
    unittest.main