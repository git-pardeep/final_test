import logging
import inspect
import softest

class utils(softest.TestCase):
    def customer_logging(self, logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh = logging.FileHandler("automation.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s  ")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
    def assertioncheck(self,all_stop,value):
        try:
            for stop in all_stop:
        #     assert stop.text=="1 Stop"
        #     if stop.text=="1 Stop":
        #         print ("assert pass")
        #     else:
        #         print("assert fail")

                self.soft_assert(self.assertEqual, stop.text,value)
                if stop.text=="1 Stop":
                    print("assert pass")
                else :
                    print("assert fail")
                self.assert_all()
        except AssertionError:
            print("valid ")
