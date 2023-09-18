import pandas
import api_wrapper

class FileMerger:
    def __init__(self, http_wrapper):
        self.api_wrapper = http_wrapper

    def merge_files(self, file_paths):
        result = ''
        for file_path in file_paths:
            if isinstance(result, pandas.DataFrame):
                df = pandas.read_csv(file_path)
                result = result.merge(df, how='inner', on = 'user_id')
            else:
                result = pandas.read_csv(file_path)

        wrapper = self.api_wrapper('o1sRRZSLlw', 'xeYjNEhmutkgkqCZyhBn6DErVntAKDx30FqFOS6D')
        final = wrapper.fix_users(result)

        return final

FileMerger_obj = FileMerger(api_wrapper.piano_wrapper)
merged_file = FileMerger_obj.merge_files(['filea.csv', 'fileb.csv'])
merged_file.to_csv('merged_file.csv', index = False)