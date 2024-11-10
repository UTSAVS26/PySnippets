import time

def time_my_func(my_func):
    def timed(*args, **kwargs):
        """
        Decorates a function to print its execution time.
        """
        message_top = "\nStarting {}".format(my_func.__name__)
        print(message_top)
        print("-" * len(message_top))
        t0 = time.time()

        result = my_func(*args, **kwargs)

        message_bot = "\nCompleted in {:.2f} minutes.".format((time.time() - t0)/60)
        print(message_bot)
        print('-' * len(message_bot))
        return result
    return timed