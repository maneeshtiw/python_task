from collections import Counter


class Solution:

    def __init__(self):
        pass

    def max_tweets(self):
        try:
            tweet_names = self.get_tweet_names()
            uniqe_names = [i.split()[0] for
                          i in tweet_names]
            times = Counter(uniqe_names)
            repeat = times.values()

            for x in set(repeat):
                duplicate = ([(key, value) for
                         key, value in sorted(times.items()) if
                         value == x])

                if len(duplicate) > 1:
                    for (key, value) in duplicate:
                        print(key, '', value)
                max_value = max(times.values())
                temp_max_result = [(key, value) for
                                   key, value in sorted(times.items()) if
                                   value == max_value]

                if temp_max_result != duplicate:
                    for (key, value) in temp_max_result:
                        print(key, '', value)

                else:
                    print("There is equal number of tweets")

        except Exception as e:
            pass

    def get_tweet_names(self):

        try:
            test_case = int(input("Enter the number of test cases you want :"))
            tweet_names = []
            for i in range(test_case):
                try:
                    no = int(input("Enter the number of tweets:"))

                except Exception as e:
                    print("Please enter the number of tweets...!")
                    no = int(input("Enter the number of tweets:"))

                try:

                    for i in range(no):
                        names = input("Enter name and tweet id :")
                        names = names.lower()
                        tweet_names.append(names)
                except Exception as e:
                    pass

            return tweet_names

        except Exception as e:
            pass


if __name__ == '__main__':
    obj = Solution()
    obj.max_tweets()
