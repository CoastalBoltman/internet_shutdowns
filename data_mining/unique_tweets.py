class FilterUnique:
    def __init__(self, aggregate_data):
        self.aggregate_data = aggregate_data

    def unique_tweets(self):
        nlp_data = {}

        for tweet_item in self.aggregate_data:
            if tweet_item["data-item-id"] not in nlp_data:
                nlp_data[tweet_item["data-item-id"]] = (
                    tweet_item["date"],
                    tweet_item["tweet"],
                )

        return nlp_data

