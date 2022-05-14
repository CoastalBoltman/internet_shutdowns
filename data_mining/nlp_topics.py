class NLPTweets:
    def __init__(self, topical_evaluation_data):
        self.topical_evaluation_data = topical_evaluation_data

    def nineties_rap(self):
        nlp_df = pd.DataFrame.from_dict(self.topical_evaluation_data, orient="index")
        nlp_df = nlp_df.reset_index()
        nlp_df.rename(
            columns={
                nlp_df.columns[0]: "tweet_id",
                nlp_df.columns[1]: "tweet_date",
                nlp_df.columns[2]: "tweet_data",
            },
            inplace=True,
        )

        return nlp_df

