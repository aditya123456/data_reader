from xlrd import open_workbook
import json

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
        print ("before flag")
        print (dict_list)
        for i in dict_list:
            if i['executionFlag'] == FLAG:
                filter_list.append(i)
        print ("after flag")
        print (filter_list)
        # print dict_list
        return filter_list


    def put_values_in_json_with_json_file(self, file_name, index):
        json_res=''
        try:
            json_res = json.loads(open(file_name).read())
        except:
            print ("file does not exist")
        data = json_res['data']
        try:
            for i in data:
                for json_key ,json_value in i.items():
                    try:
                        for excel_key,excel_value in index.items():
                            if excel_key == json_value:
                                i[json_key] = excel_value
                    except:
                        pass
        except:
            pass
        print (json.dumps(json_res))
        return json.dumps(json_res)



if __name__ == '__main__':
    x = EXCELLibray()
    x.Datareader('sample.xlsx', 'Y')
	x.put_values_in_json_with_json_file('sample.json', {"email":"email2"})
