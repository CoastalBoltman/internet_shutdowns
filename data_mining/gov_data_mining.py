import os.path
import os.path
import logging
import time
import random
import twint
import nest_asyncio
from datetime import datetime, timedelta, date


class GovShutdownDataMining:
    def __init__(self, twint_search, start_date, end_date, limit):
        self.twint_search = twint_search
        self.start_date = start_date
        self.end_date = end_date
        self.limit = limit
        self.time_interval_seconds = (
            600  # 10 minute intervals unless specified otherwise
        )

    def sleeping(self):
        """Sleeps the Twint request for a random amount of time"""
        random_list = random.sample(range(5), 1)

        return random.choice(random_list)

    def second_search(self):
        """Developing second increments to perform search function"""
        return np.arange(
            0,
            (self.end_date - self.start_date).total_seconds(),
            self.time_interval_seconds,
        ).tolist()

    def twint_load(self, filename_date, tweet_list):
        """Pushing data to local file. This can be scoped to be pushed to S3"""
        directory = "/home/ramy/gov_shutdown/tweet_second_data"
        filename = filename_date
        file_path = os.path.join(directory, filename)

        with open(file_path, "w") as f:
            for item in tweet_list:
                f.write("%s\n" % item)

    def twint_data(self):
        tweet_list_output = []
        start_time = datetime.strftime(self.start_date, "%Y-%m-%d %H:%M:%S")
        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        time_interval_seconds = self.time_interval_seconds

        for time_increments in self.second_search():
            start_search = start_time + timedelta(seconds=time_increments)
            end_search = start_search + timedelta(seconds=self.time_interval_seconds)
            start_search = datetime.strftime(start_search, "%Y-%m-%d %H:%M:%S")
            end_search = datetime.strftime(end_search, "%Y-%m-%d %H:%M:%S")
            print(
                f"----You are now generating twitter information on {self.twint_search} for {start_search} to {end_search}-----------------"
            )
            c = twint.Config()
            c.Search = self.twint_search
            c.Store_object = True
            c.Since = start_search
            c.Until = end_search
            c.Limit = self.limit
            twint.run.Search(c)
            tlist = c.search_tweet_list
            self.twint_load(start_search, tlist)
            time.sleep(self.sleeping())

        print(
            f"------Completed data retrieval for {self.start_date} to {self.end_date} with 10 minute intervals----------"
        )

        return tlist



