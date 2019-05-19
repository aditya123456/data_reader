
from xlrd import open_workbook

class EXCELLibray(object):

    
    def Datareader(self, file_name,  FLAG):
        filter_list =[]
        book = open_workbook(file_name)
        sheet = book.sheet_by_index(0)

        # read header values into the list
        keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
        print keys

        dict_list = []
        for row_index in range(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value for col_index in range(sheet.ncols)}
            dict_list.append(d)
        print "before flag"
        print dict_list
        for i in dict_list:
            if i['executionFlag'] == FLAG:
                filter_list.append(i)
        print "after flag"
        print filter_list
        # print dict_list
        return filter_list

    def put_values_in_json(self, email1):
        sample_json1={  "id": 4, "email": "<email1>","first_name": "Eve", "last_name": "Holt", "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/marcoramires/128.jpg"
        }
        for k, v in sample_json1.items():
            if v == '<email1>':
                sample_json1[k]=email1
        print sample_json1
        # sample_json = {"name1":{"firstName":firstName, "lastName":lastName, "value1":value1, "value2":value2},
        #               "name2":{"firstName":firstName, "lastName":lastName, "value1":value1, "value2":value2}}
        return sample_json1



if __name__ == '__main__':
    x = EXCELLibray()
    x.Datareader('sample.xlsx', 'Y')