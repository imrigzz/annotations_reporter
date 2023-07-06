import unittest
import pandas as pd
from main_report import get_annotator_counts,get_missing_annotators
from main_total_payment import total_payment

class TestMain(unittest.TestCase):
    def test_get_annotator_counts(self):
        # Call the function under test
        result = get_annotator_counts("test_data.jsonl")
        # Define the expected result
        expected_result = {
            "line_segments-nyibum": {
                "accept": {"counts": 5, "image_id": ['I4PD9040711.jpg_2000x700.jpg']},
                "reject": {"counts": 2, "image_id": ['I3CN31331046.jpg_2000x700.jpg','I1PD360790137.tif_2000x700.png']},
                "ignore": {"counts": 2, "image_id": ['I4PD9050391.jpg_2000x700.jpg','I4PD9050461.jpg_2000x700.jpg']},
                "no_span": {"counts": 1, "image_id": ['I3CN31310697.jpg_2000x700.jpg']}
            },
            "line_segments-palden": {
                "accept": {"counts": 0, "image_id": []},
                "reject": {"counts": 1, "image_id": ['I4PD9060212.jpg_2000x700.jpg']},
                "ignore": {"counts": 1, "image_id": ['I4PD9060359.jpg_2000x700.jpg']},
                "no_span": {"counts": 1, "image_id": ['I3CN31300311.jpg_2000x700.jpg']}
            }
        }
        # Assert that the actual result matches the expected result
        self.assertEqual(result, expected_result)

    def test_get_missing_annotators(self):
        # Call the function under test
        result = get_missing_annotators("test_data.jsonl")

        # Define the expected result
        expected_result = ['I3CN31310924.jpg_2000x700.jpg','I3CN31330776.jpg_2000x700.jpg']

        # Assert that the actual result matches the expected result
        self.assertEqual(result, expected_result)

    def test_total_payment(self):
        # Call the function under test
        rate = 5
        file_path = "outputs/annotators_report.csv"
        result = total_payment(file_path,rate)

        # Define the expected result
        data = {
            'annotator_id':['line_segments-nyibum','line_segments-palden'],
            'accept counts':[5,0],
            'recject counts':[2,1],
            'ignore counts':[2,1],
            'no_span counts':[1,1],
            'Total_payment':[25,0]
        }
        expected_result = pd.DataFrame(data)

        # Assert that the actual result matches the expected result
        self.assertEqual(True, result.equals(expected_result))


if __name__ == "__main__":
    unittest.main()
