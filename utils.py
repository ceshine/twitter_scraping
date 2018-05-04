import pandas as pd


def get_urls(df):
    return df.apply(
        lambda row:
        f"https://twitter.com/{row['screen_name']}/status/{row['id_str']}",
        axis=1
    )
