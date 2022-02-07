import mysql.connector
from mysql.connector import Error


def dbConnect(user_id, username, tweet_id, tweet, retweet_count, hashtags) -> None:
    """
    Connects to the mysql DB and inserts the tweet data
    :param user_id:
    :param username:
    :param tweet_id:
    :param tweet:
    :param retweet_count:
    :param hashtags:
    :return:
    """
    try:
        con = mysql.connector.connect(host='localhost',
                database='TwitterDB', user='root', password='password', charset='utf8')
        print("connected to database")

        if con.is_connected():
            """
            Insert twitter data
            """
            print(id, user_id, username, tweet_id, tweet, retweet_count, ",".join(hashtags))
            hashtags = ",".join(hashtags)
            cursor = con.cursor()
            try:
                query = f"INSERT INTO tweet_data (tweet_id, user_id, username, tweet, retweet_count, hashtags) VALUES ( %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (tweet_id, user_id, username, tweet, retweet_count, hashtags))
                print("Inserted one row")
            except Exception as e:
                print(e)
                pass
            con.commit()


    except Error as e:
        print(e)

    con.close()

    return
