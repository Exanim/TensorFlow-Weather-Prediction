import unittest
import pandas as pd
from model.csv_cleaner import replace_missing_values  # Import your actual module


class TestReplaceMissingValues(unittest.TestCase):
    def setUp(self):
        # Create a sample CSV file for testing
        self.sample_csv = "test_data.csv"
        data = {"Column1": [1, 2, "hiány", 4, 5],
                "Column2": [10, "hiány", 30, 40, 50]}
        df = pd.DataFrame(data)
        df.to_csv(self.sample_csv, index=False)

    def tearDown(self):
        # Clean up the sample CSV file after the test
        import os
        os.remove(self.sample_csv)

    def test_replace_missing_values_should_not_contain_na(self):
        result_df = replace_missing_values(self.sample_csv)

        nan_check = not result_df.isna().any().any()
        self.assertTrue(nan_check)

    def test_replace_missing_values_should_remove_hiany(self):
        result_df = replace_missing_values(self.sample_csv)
        
        self.assertNotIn("hiány", result_df.values)

    def test_replace_missing_values_should_be_numeric(self):
        result_df = replace_missing_values(self.sample_csv)

        numeric_check = pd.to_numeric(result_df.stack(), errors='coerce').notna().all()
        self.assertTrue(numeric_check)


if __name__ == '__main__':
    unittest.main()
