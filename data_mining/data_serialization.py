import os
import pickle
from datetime import datetime, timedelta, date


class AggregatingData:
    def __init__(
        self, file_directory, start_date, end_date
    ):  # date format is date(2020,1,1)
        self.file_directory = file_directory
        self.start_date = start_date
        self.end_date = end_date

    def date_generator(self):

        for n in range(int((self.end_date - self.start_date).days)):
            yield self.start_date + timedelta(n)

    def date_list(self):
        date_names = []

        for dates in self.date_generator():
            dates = datetime.strftime(dates, "%Y-%m-%d")
            date_names.append(dates)

        return date_names

    def pickle_jar(self):
        aggregated_nlp_data = []

        for pickles in self.date_list():
            file_name = pickles
            file_path = os.path.join(self.file_directory, file_name)

            with open(file_path, "rb") as handle:
                unserialized = pickle.load(handle)
                aggregated_nlp_data.extend(unserialized)

        return aggregated_nlp_data

