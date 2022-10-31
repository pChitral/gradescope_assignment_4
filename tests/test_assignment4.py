import unittest
import assignment4
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestAssignment4(unittest.TestCase):
    def setUp(self):
        self.assignment4 = assignment4

    @weight(3)
    @visibility('visible')
    @number("1.1")
    def test_IteratorClass_1(self):
        self.assertRaises(ValueError, assignment4.IteratorClass,
                          range(5, 10), [1, 2, 3], 'div')

    @weight(3)
    @visibility('visible')
    @number("1.2")
    def test_IteratorClass_2(self):
        self.assertRaises(ValueError, assignment4.IteratorClass, [
                          1, 2, 3], range(5, 10), 'div')

    @weight(3)
    @visibility('visible')
    @number("1.3")
    def test_IteratorClass_3(self):
        self.assertRaises(ValueError, assignment4.IteratorClass, [
                          1, 2, 3], [1, 2, 3], 'abc')

    @weight(3)
    @visibility('visible')
    @number("1.4")
    def test_IteratorClass_4(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        add_iterator = assignment4.IteratorClass(x, y, 'add')
        self.assertEqual([ele for ele in add_iterator], [55, 57, 59, 61, 63])

    @weight(3)
    @visibility('visible')
    @number("1.5")
    def test_IteratorClass_5(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        sub_iterator = assignment4.IteratorClass(x, y, 'sub')
        self.assertEqual([ele for ele in sub_iterator],
                         [-45, -45, -45, -45, -45])

    @weight(3)
    @visibility('visible')
    @number("1.6")
    def test_IteratorClass_6(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        mul_iterator = assignment4.IteratorClass(x, y, 'mul')
        self.assertEqual([ele for ele in mul_iterator],
                         [250, 306, 364, 424, 486])

    @weight(3)
    @visibility('visible')
    @number("1.7")
    def test_IteratorClass_7(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        div_iterator = assignment4.IteratorClass(x, y, 'div')
        self.assertEqual([ele for ele in div_iterator],
                         [0.1, 0.12, 0.13, 0.15, 0.17])

    @weight(3)
    @visibility('visible')
    @number("1.8")
    def test_IteratorClass_8(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        div_iterator = assignment4.IteratorClass(x, y, 'div')
        self.assertEqual(hasattr(div_iterator.__class__, '__next__'), True)

    @weight(3)
    @visibility('visible')
    @number("2.1")
    def test_ListV2_1(self):
        self.assertRaises(ValueError, assignment4.ListV2,  3)

    @weight(3)
    @visibility('visible')
    @number("2.2")
    def test_ListV2_2(self):
        self.assertRaises(ValueError, assignment4.ListV2,  '3')

    @weight(3)
    @visibility('visible')
    @number("2.3")
    def test_ListV2_3(self):
        self.assertRaises(ValueError, assignment4.ListV2,  3.14)

    @weight(3)
    @visibility('visible')
    @number("2.4")
    def test_ListV2_4(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        l2 = assignment4.ListV2(list(range(50, 55)))
        result = l1 + l2
        self.assertEqual(type(result),  assignment4.ListV2)

    @weight(3)
    @visibility('visible')
    @number("2.5")
    def test_ListV2_5(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        l2 = assignment4.ListV2(list(range(50, 55)))
        result = l1 + l2
        self.assertEqual([ele for ele in result],  [55, 57, 59, 61, 63])

    @weight(3)
    @visibility('visible')
    @number("2.6")
    def test_ListV2_6(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        l2 = assignment4.ListV2(list(range(50, 55)))
        result = l1 - l2
        self.assertEqual([ele for ele in result],  [-45, -45, -45, -45, -45])

    @weight(3)
    @visibility('visible')
    @number("2.7")
    def test_ListV2_7(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        l2 = assignment4.ListV2(list(range(50, 55)))
        result = l1 * l2
        self.assertEqual([ele for ele in result],  [250, 306, 364, 424, 486])

    @weight(3)
    @visibility('visible')
    @number("2.8")
    def test_ListV2_8(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        l2 = assignment4.ListV2(list(range(50, 55)))
        result = l1 / l2
        self.assertEqual([ele for ele in result],  [
                         0.1, 0.12, 0.13, 0.15, 0.17])

    @weight(3)
    @visibility('visible')
    @number("2.9")
    def test_ListV2_9(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        result = l1 + 5
        self.assertEqual([ele for ele in result],  [10, 11, 12, 13, 14])

    @weight(3)
    @visibility('visible')
    @number("2.10")
    def test_ListV2_10(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        result = l1 - 5
        self.assertEqual([ele for ele in result],  [0, 1, 2, 3, 4])

    @weight(3)
    @visibility('visible')
    @number("2.11")
    def test_ListV2_11(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        result = l1 * 5
        self.assertEqual([ele for ele in result],  [25, 30, 35, 40, 45])

    @weight(3)
    @visibility('visible')
    @number("2.12")
    def test_ListV2_12(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        result = l1 / 5
        self.assertEqual([ele for ele in result],  [1.0, 1.2, 1.4, 1.6, 1.8])

    @weight(3)
    @visibility('visible')
    @number("2.13")
    def test_ListV2_13(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        l2 = list(range(50, 55))
        result = l1 + l2
        self.assertEqual([ele for ele in result],  [55, 57, 59, 61, 63])

    @weight(3)
    @visibility('visible')
    @number("2.14")
    def test_ListV2_14(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        l2 = list(range(50, 55))
        result = l1 - l2
        self.assertEqual([ele for ele in result],  [-45, -45, -45, -45, -45])

    @weight(3)
    @visibility('visible')
    @number("2.15")
    def test_ListV2_15(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        l2 = tuple(range(50, 55))
        result = l1 * l2
        self.assertEqual([ele for ele in result],  [250, 306, 364, 424, 486])

    @weight(3)
    @visibility('visible')
    @number("2.16")
    def test_ListV2_16(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        l2 = tuple(range(50, 55))
        result = l1 / l2
        self.assertEqual([ele for ele in result],  [0.1, 0.12, 0.13, 0.15, 0.17])

    @weight(3)
    @visibility('visible')
    @number("2.17")
    def test_ListV2_17(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        self.assertEqual(l1.__repr__(),  '[5, 6, 7, 8, 9]')

    @weight(3)
    @visibility('visible')
    @number("2.18")
    def test_ListV2_18(self):
        l1 = assignment4.ListV2(list(range(5, 10)))
        self.assertEqual(hasattr(l1.__class__, '__next__'), True)


    @weight(3)
    @visibility('visible')
    @number("3.1")
    def test_ex3_1(self):
        l_func, min_student = self.assignment4.ex3('ex3_data.txt')
        expected_value = 'student11,72,69,69,65,91'
        self.assertEqual(expected_value, min_student)

    @weight(3)
    @visibility('visible')
    @number("3.2")
    def test_ex3_2(self):
        l_func, min_student = self.assignment4.ex3('ex3_data.txt')
        lines = (
            'student45,83,74,99,76,95',
            'student46,96,83,79,89,71',
            'student47,70,85,94,73,74',
            'student48,99,72,92,65,87',
            'student49,78,93,99,77,85',
            'student50,96,91,76,72,66',
            'student51,94,86,77,91,96',
        )

        expected_value = 'student47,70,85,94,73,74'
        self.assertEqual(expected_value, min(lines, key=l_func))

    @weight(3)
    @visibility('visible')
    @number("3.3")
    def test_ex3_3(self):
        import types
        l_func, min_student = self.assignment4.ex3('ex3_data.txt')
        self.assertEqual(types.LambdaType, type(l_func))

    @weight(3)
    @visibility('visible')
    @number("4.1")
    def test_ex4_1(self):
        import types
        l_func, student_grades = self.assignment4.ex4('ex3_data.txt')
        expected_value = ['student1: B',
                          'student2: B',
                          'student3: B',
                          'student4: B',
                          'student5: B',
                          'student6: B',
                          'student7: C',
                          'student8: C',
                          'student9: B',
                          'student10: C',
                          'student11: C',
                          'student12: C',
                          'student13: B',
                          'student14: B',
                          'student15: C',
                          'student16: B',
                          'student17: B',
                          'student18: B',
                          'student19: C',
                          'student20: B',
                          'student21: B',
                          'student22: C',
                          'student23: B',
                          'student24: B',
                          'student25: A',
                          'student26: B',
                          'student27: C',
                          'student28: B',
                          'student29: B',
                          'student30: B',
                          'student31: B',
                          'student32: C',
                          'student33: B',
                          'student34: B',
                          'student35: B',
                          'student36: C',
                          'student37: B',
                          'student38: B',
                          'student39: C',
                          'student40: C',
                          'student41: B',
                          'student42: A',
                          'student43: B',
                          'student44: C',
                          'student45: B',
                          'student46: B',
                          'student47: C',
                          'student48: B',
                          'student49: B',
                          'student50: B',
                          'student51: B',
                          'student52: C',
                          'student53: B',
                          'student54: C',
                          'student55: A',
                          'student56: A',
                          'student57: B',
                          'student58: C',
                          'student59: B',
                          'student60: B',
                          'student61: B',
                          'student62: B',
                          'student63: B',
                          'student64: B',
                          'student65: C',
                          'student66: C',
                          'student67: C',
                          'student68: B',
                          'student69: B',
                          'student70: B',
                          'student71: B',
                          'student72: C',
                          'student73: B',
                          'student74: B',
                          'student75: B',
                          'student76: B',
                          'student77: B',
                          'student78: C',
                          'student79: B',
                          'student80: B',
                          'student81: B',
                          'student82: C',
                          'student83: B',
                          'student84: C',
                          'student85: C',
                          'student86: B',
                          'student87: A',
                          'student88: B',
                          'student89: C',
                          'student90: B',
                          'student91: B',
                          'student92: C',
                          'student93: C',
                          'student94: C',
                          'student95: A',
                          'student96: B',
                          'student97: A',
                          'student98: B',
                          'student99: C',
                          'student100: B']

        self.assertEqual(expected_value, list(student_grades))

    @weight(3)
    @visibility('visible')
    @number("4.2")
    def test_ex4_2(self):
        import types
        l_func, student_grades = self.assignment4.ex4('ex3_data.txt')
        self.assertEqual(types.LambdaType, type(l_func))

    @weight(3)
    @visibility('visible')
    @number("4.3")
    def test_ex4_3(self):
        l_func, student_grades = self.assignment4.ex4('ex3_data.txt')
        lines = (
            'student45,83,74,99,76,95',
            'student46,96,83,79,89,71',
            'student47,70,85,94,73,74',
            'student48,99,72,92,65,87',
            'student49,78,93,99,77,85',
            'student50,96,91,76,72,66',
            'student51,94,86,77,91,96',
        )

        expected_value = [
            'student45: B',
            'student46: B',
            'student47: C',
            'student48: B',
            'student49: B',
            'student50: B',
            'student51: B'
        ]

        self.assertEqual(expected_value, list(map(l_func, lines)))

    @weight(3)
    @visibility('visible')
    @number("5.1")
    def test_ex5_1(self):
        l_func, output = self.assignment4.ex5('grades_dict.json')

        expected_value = [
            {'name': 'student2', 'test1': '100', 'test2': '90',
                'test3': '65', 'test4': '68', 'test5': '94'},
            {'name': 'student83', 'test1': '88', 'test2': '76',
                'test3': '65', 'test4': '97', 'test5': '82'},
            {'name': 'student31', 'test1': '90', 'test2': '87',
                'test3': '66', 'test4': '95', 'test5': '72'},
            {'name': 'student43', 'test1': '86', 'test2': '69',
                'test3': '66', 'test4': '70', 'test5': '74'},
            {'name': 'student47', 'test1': '93', 'test2': '78',
                'test3': '67', 'test4': '74', 'test5': '74'},
            {'name': 'student52', 'test1': '83', 'test2': '78',
                'test3': '67', 'test4': '71', 'test5': '65'},
            {'name': 'student37', 'test1': '91', 'test2': '78',
                'test3': '68', 'test4': '67', 'test5': '92'},
            {'name': 'student58', 'test1': '89', 'test2': '88',
                'test3': '68', 'test4': '79', 'test5': '79'},
            {'name': 'student63', 'test1': '85', 'test2': '66',
                'test3': '69', 'test4': '74', 'test5': '69'},
            {'name': 'student12', 'test1': '88', 'test2': '83',
                'test3': '71', 'test4': '89', 'test5': '73'},
            {'name': 'student85', 'test1': '76', 'test2': '100',
                'test3': '71', 'test4': '69', 'test5': '65'},
            {'name': 'student98', 'test1': '81', 'test2': '85',
                'test3': '71', 'test4': '89', 'test5': '76'},
            {'name': 'student17', 'test1': '86', 'test2': '98',
                'test3': '73', 'test4': '100', 'test5': '92'},
            {'name': 'student62', 'test1': '86', 'test2': '100',
                'test3': '73', 'test4': '99', 'test5': '76'},
            {'name': 'student69', 'test1': '93', 'test2': '95',
                'test3': '73', 'test4': '86', 'test5': '90'},
            {'name': 'student81', 'test1': '95', 'test2': '83',
                'test3': '74', 'test4': '75', 'test5': '81'},
            {'name': 'student93', 'test1': '95', 'test2': '97',
                'test3': '74', 'test4': '74', 'test5': '81'},
            {'name': 'student26', 'test1': '80', 'test2': '78',
                'test3': '75', 'test4': '69', 'test5': '87'},
            {'name': 'student34', 'test1': '93', 'test2': '88',
                'test3': '77', 'test4': '67', 'test5': '93'},
            {'name': 'student14', 'test1': '85', 'test2': '97',
                'test3': '78', 'test4': '67', 'test5': '99'},
            {'name': 'student79', 'test1': '91', 'test2': '94',
                'test3': '78', 'test4': '83', 'test5': '92'},
            {'name': 'student25', 'test1': '77', 'test2': '86',
                'test3': '79', 'test4': '70', 'test5': '92'},
            {'name': 'student55', 'test1': '91', 'test2': '76',
                'test3': '79', 'test4': '65', 'test5': '66'},
            {'name': 'student70', 'test1': '100', 'test2': '71',
                'test3': '79', 'test4': '99', 'test5': '78'},
            {'name': 'student80', 'test1': '98', 'test2': '85',
                'test3': '79', 'test4': '91', 'test5': '92'},
            {'name': 'student13', 'test1': '95', 'test2': '72',
                'test3': '80', 'test4': '73', 'test5': '84'},
            {'name': 'student35', 'test1': '75', 'test2': '89',
                'test3': '80', 'test4': '93', 'test5': '74'},
            {'name': 'student20', 'test1': '68', 'test2': '68',
                'test3': '81', 'test4': '74', 'test5': '76'},
            {'name': 'student50', 'test1': '94', 'test2': '68',
                'test3': '81', 'test4': '69', 'test5': '89'},
            {'name': 'student66', 'test1': '91', 'test2': '92',
                'test3': '81', 'test4': '79', 'test5': '69'},
            {'name': 'student1', 'test1': '73', 'test2': '91',
                'test3': '82', 'test4': '90', 'test5': '93'},
            {'name': 'student100', 'test1': '79', 'test2': '79',
                'test3': '82', 'test4': '71', 'test5': '87'},
            {'name': 'student5', 'test1': '86', 'test2': '93',
                'test3': '83', 'test4': '94', 'test5': '94'},
            {'name': 'student16', 'test1': '81', 'test2': '95',
                'test3': '83', 'test4': '87', 'test5': '95'},
            {'name': 'student19', 'test1': '70', 'test2': '70',
                'test3': '83', 'test4': '99', 'test5': '97'},
            {'name': 'student61', 'test1': '65', 'test2': '76',
                'test3': '83', 'test4': '75', 'test5': '68'},
            {'name': 'student91', 'test1': '79', 'test2': '100',
                'test3': '83', 'test4': '66', 'test5': '69'},
            {'name': 'student96', 'test1': '99', 'test2': '93',
                'test3': '83', 'test4': '75', 'test5': '85'},
            {'name': 'student21', 'test1': '74', 'test2': '73',
                'test3': '84', 'test4': '84', 'test5': '69'},
            {'name': 'student46', 'test1': '92', 'test2': '83',
                'test3': '84', 'test4': '69', 'test5': '90'},
            {'name': 'student22', 'test1': '65', 'test2': '87',
                'test3': '85', 'test4': '78', 'test5': '98'},
            {'name': 'student23', 'test1': '88', 'test2': '95',
                'test3': '85', 'test4': '67', 'test5': '93'},
            {'name': 'student72', 'test1': '85', 'test2': '66',
                'test3': '85', 'test4': '78', 'test5': '75'},
            {'name': 'student82', 'test1': '77', 'test2': '100',
                'test3': '85', 'test4': '65', 'test5': '80'},
            {'name': 'student88', 'test1': '77', 'test2': '87',
                'test3': '85', 'test4': '90', 'test5': '78'},
            {'name': 'student18', 'test1': '65', 'test2': '78',
                'test3': '86', 'test4': '69', 'test5': '98'},
            {'name': 'student24', 'test1': '80', 'test2': '91',
                'test3': '86', 'test4': '99', 'test5': '96'},
            {'name': 'student28', 'test1': '90', 'test2': '100',
                'test3': '86', 'test4': '89', 'test5': '75'},
            {'name': 'student53', 'test1': '83', 'test2': '100',
                'test3': '86', 'test4': '83', 'test5': '90'},
            {'name': 'student74', 'test1': '97', 'test2': '99',
                'test3': '86', 'test4': '93', 'test5': '99'},
            {'name': 'student75', 'test1': '79', 'test2': '79',
                'test3': '86', 'test4': '78', 'test5': '68'},
            {'name': 'student78', 'test1': '88', 'test2': '98',
                'test3': '86', 'test4': '100', 'test5': '71'},
            {'name': 'student90', 'test1': '95', 'test2': '66',
                'test3': '86', 'test4': '85', 'test5': '65'},
            {'name': 'student10', 'test1': '98', 'test2': '68',
                'test3': '87', 'test4': '85', 'test5': '96'},
            {'name': 'student27', 'test1': '94', 'test2': '99',
                'test3': '87', 'test4': '91', 'test5': '86'},
            {'name': 'student42', 'test1': '72', 'test2': '86',
                'test3': '87', 'test4': '98', 'test5': '73'},
            {'name': 'student49', 'test1': '81', 'test2': '98',
                'test3': '87', 'test4': '81', 'test5': '79'},
            {'name': 'student84', 'test1': '70', 'test2': '66',
                'test3': '87', 'test4': '100', 'test5': '97'},
            {'name': 'student33', 'test1': '95', 'test2': '67',
                'test3': '88', 'test4': '81', 'test5': '97'},
            {'name': 'student38', 'test1': '68', 'test2': '98',
                'test3': '88', 'test4': '84', 'test5': '72'},
            {'name': 'student45', 'test1': '91', 'test2': '81',
                'test3': '88', 'test4': '95', 'test5': '69'},
            {'name': 'student64', 'test1': '89', 'test2': '78',
                'test3': '88', 'test4': '86', 'test5': '95'},
            {'name': 'student86', 'test1': '81', 'test2': '71',
                'test3': '88', 'test4': '98', 'test5': '81'},
            {'name': 'student76', 'test1': '80', 'test2': '72',
                'test3': '89', 'test4': '88', 'test5': '89'},
            {'name': 'student77', 'test1': '84', 'test2': '99',
                'test3': '89', 'test4': '69', 'test5': '66'},
            {'name': 'student92', 'test1': '88', 'test2': '91',
                'test3': '89', 'test4': '97', 'test5': '99'},
            {'name': 'student3', 'test1': '94', 'test2': '67',
                'test3': '90', 'test4': '95', 'test5': '84'},
            {'name': 'student40', 'test1': '94', 'test2': '97',
                'test3': '90', 'test4': '95', 'test5': '84'},
            {'name': 'student11', 'test1': '92', 'test2': '81',
                'test3': '91', 'test4': '96', 'test5': '78'},
            {'name': 'student57', 'test1': '87', 'test2': '84',
                'test3': '91', 'test4': '83', 'test5': '80'},
            {'name': 'student87', 'test1': '88', 'test2': '100',
                'test3': '91', 'test4': '75', 'test5': '66'},
            {'name': 'student44', 'test1': '67', 'test2': '100',
                'test3': '92', 'test4': '87', 'test5': '80'},
            {'name': 'student68', 'test1': '78', 'test2': '99',
                'test3': '92', 'test4': '74', 'test5': '89'},
            {'name': 'student89', 'test1': '82', 'test2': '78',
                'test3': '92', 'test4': '90', 'test5': '99'},
            {'name': 'student97', 'test1': '87', 'test2': '82',
                'test3': '92', 'test4': '88', 'test5': '92'},
            {'name': 'student8', 'test1': '88', 'test2': '71',
                'test3': '93', 'test4': '71', 'test5': '86'},
            {'name': 'student59', 'test1': '78', 'test2': '76',
                'test3': '94', 'test4': '65', 'test5': '80'},
            {'name': 'student60', 'test1': '67', 'test2': '76',
                'test3': '94', 'test4': '67', 'test5': '74'},
            {'name': 'student15', 'test1': '84', 'test2': '71',
                'test3': '95', 'test4': '77', 'test5': '77'},
            {'name': 'student29', 'test1': '89', 'test2': '93',
                'test3': '95', 'test4': '78', 'test5': '82'},
            {'name': 'student67', 'test1': '74', 'test2': '80',
                'test3': '95', 'test4': '85', 'test5': '94'},
            {'name': 'student94', 'test1': '80', 'test2': '71',
                'test3': '95', 'test4': '76', 'test5': '68'},
            {'name': 'student32', 'test1': '91', 'test2': '76',
                'test3': '96', 'test4': '73', 'test5': '91'},
            {'name': 'student51', 'test1': '94', 'test2': '93',
                'test3': '96', 'test4': '96', 'test5': '76'},
            {'name': 'student73', 'test1': '92', 'test2': '89',
                'test3': '96', 'test4': '83', 'test5': '79'},
            {'name': 'student99', 'test1': '69', 'test2': '74',
                'test3': '96', 'test4': '97', 'test5': '71'},
            {'name': 'student39', 'test1': '75', 'test2': '90',
                'test3': '97', 'test4': '86', 'test5': '72'},
            {'name': 'student56', 'test1': '98', 'test2': '80',
                'test3': '97', 'test4': '68', 'test5': '91'},
            {'name': 'student4', 'test1': '68', 'test2': '85',
                'test3': '98', 'test4': '69', 'test5': '77'},
            {'name': 'student30', 'test1': '66', 'test2': '92',
                'test3': '98', 'test4': '92', 'test5': '100'},
            {'name': 'student41', 'test1': '71', 'test2': '77',
                'test3': '98', 'test4': '95', 'test5': '70'},
            {'name': 'student54', 'test1': '92', 'test2': '72',
                'test3': '98', 'test4': '70', 'test5': '98'},
            {'name': 'student71', 'test1': '95', 'test2': '98',
                'test3': '98', 'test4': '98', 'test5': '75'},
            {'name': 'student95', 'test1': '78', 'test2': '71',
                'test3': '98', 'test4': '78', 'test5': '96'},
            {'name': 'student6', 'test1': '72', 'test2': '97',
                'test3': '99', 'test4': '69', 'test5': '83'},
            {'name': 'student9', 'test1': '79', 'test2': '69',
                'test3': '99', 'test4': '73', 'test5': '76'},
            {'name': 'student7', 'test1': '66', 'test2': '99',
                'test3': '100', 'test4': '96', 'test5': '81'},
            {'name': 'student36', 'test1': '76', 'test2': '69',
                'test3': '100', 'test4': '97', 'test5': '83'},
            {'name': 'student48', 'test1': '98', 'test2': '69',
                'test3': '100', 'test4': '84', 'test5': '80'},
            {'name': 'student65', 'test1': '80', 'test2': '75',
                'test3': '100', 'test4': '83', 'test5': '77'}
        ]
        self.assertEqual(expected_value, output)

    @weight(3)
    @visibility('visible')
    @number("5.2")
    def test_ex5_2(self):
        import types
        l_func, output = self.assignment4.ex5('grades_dict.json')
        self.assertEqual(types.LambdaType, type(l_func))

    @weight(3)
    @visibility('visible')
    @number("5.3")
    def test_ex5_3(self):
        import types
        l_func, output = self.assignment4.ex5('grades_dict.json')
        lines = [{
            "name": "student19",
            "test1": "70",
            "test2": "70",
            "test3": "83",
            "test4": "99",
            "test5": "97"
        },
            {
            "name": "student20",
            "test1": "68",
            "test2": "68",
            "test3": "81",
            "test4": "74",
            "test5": "76"
        },
            {
            "name": "student21",
            "test1": "74",
            "test2": "73",
            "test3": "84",
            "test4": "84",
            "test5": "69"
        },
            {
            "name": "student22",
            "test1": "65",
            "test2": "87",
            "test3": "85",
            "test4": "78",
            "test5": "98"
        },
            {
            "name": "student23",
            "test1": "88",
            "test2": "95",
            "test3": "85",
            "test4": "67",
            "test5": "93"
        },
            {
            "name": "student24",
            "test1": "80",
            "test2": "91",
            "test3": "86",
            "test4": "99",
            "test5": "96"
        },
            {
            "name": "student25",
            "test1": "77",
            "test2": "86",
            "test3": "79",
            "test4": "70",
            "test5": "92"
        },
            {
            "name": "student26",
            "test1": "80",
            "test2": "78",
            "test3": "75",
            "test4": "69",
            "test5": "87"
        }, ]

        expected_value = [{'name': 'student26', 'test1': '80', 'test2': '78', 'test3': '75', 'test4': '69', 'test5': '87'},
                          {'name': 'student25', 'test1': '77', 'test2': '86',
                              'test3': '79', 'test4': '70', 'test5': '92'},
                          {'name': 'student20', 'test1': '68', 'test2': '68',
                              'test3': '81', 'test4': '74', 'test5': '76'},
                          {'name': 'student19', 'test1': '70', 'test2': '70',
                           'test3': '83', 'test4': '99', 'test5': '97'},
                          {'name': 'student21', 'test1': '74', 'test2': '73',
                           'test3': '84', 'test4': '84', 'test5': '69'},
                          {'name': 'student22', 'test1': '65', 'test2': '87',
                           'test3': '85', 'test4': '78', 'test5': '98'},
                          {'name': 'student23', 'test1': '88', 'test2': '95',
                           'test3': '85', 'test4': '67', 'test5': '93'},
                          {'name': 'student24', 'test1': '80', 'test2': '91', 'test3': '86', 'test4': '99', 'test5': '96'}]

        self.assertEqual(expected_value, sorted(lines, key=l_func))
