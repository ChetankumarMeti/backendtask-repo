import requests

class ApiParser:

    def __init__(self, api_link):
        self.link = api_link
        self.json_file = {}
        self.list_paid_conferences = []
        self.list_free_conferences = []
        self.map_dict_paid = {}
        self.map_dict_free = {}


    # method get list of conferences in json format
    def get_jsonfile(self):
        responce = requests.get(self.link)
        self.json_file = responce.json()
        # print(self.json_file)

    # method to convert json format to human readable format
    def convert_jsonfile(self):
        print("List of upcoming Paid technical conferences")
        for i in range(len(self.json_file['paid'])):
            paid_list = self.json_file['paid'][i]
            self.list_paid_conferences.append(f"{i + 1}.'{paid_list['confName']}', {paid_list['confStartDate']}, {paid_list['city']}, {paid_list['state']},"
                f"{paid_list['country']}, {paid_list['entryType']}, {paid_list['confRegUrl']}")

            # print human readable information
            print(f"{i+1}.'{paid_list['confName']}', {paid_list['confStartDate']}, {paid_list['city']}, {paid_list['state']},"
                  f" {paid_list['country']}, {paid_list['entryType']}, {paid_list['confRegUrl']}")

        print("List of upcoming Free technical conferences")
        for i in range(len(self.json_file['free'])):
            free_list = self.json_file['free'][i]
            self.list_free_conferences.append(f"{i + 1}.'{free_list['confName']}', {free_list['confStartDate']}, {free_list['city']}, {free_list['state']},"
                f"{free_list['country']}, {free_list['entryType']}, {free_list['confRegUrl']}")

            # print human readable information
            print(f"{i+1}.'{free_list['confName']}', {free_list['confStartDate']}, {free_list['city']}, {free_list['state']},"
                  f" {free_list['country']}, {free_list['entryType']}, {free_list['confRegUrl']}")

    # method to check duplicates present in list
    def duplicate_check(self):

        for i in range(len(self.list_paid_conferences)):
            if self.list_paid_conferences[i] in self.map_dict_paid :
                return self.list_paid_conferences[i] # return duplicate list (if any)
            self.map_dict_paid[self.list_paid_conferences[i]] = i


        for i in range(len(self.list_free_conferences)):
            if self.list_free_conferences[i] in self.map_dict_free :
                return self.list_free_conferences[i] # return duplicate list (if any)
            self.map_dict_free[self.list_free_conferences[i]] = i


# input link for API
input_link = 'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences'
api_parser = ApiParser(input_link)
api_parser.get_jsonfile()
api_parser.convert_jsonfile()

duplicate_list = api_parser.duplicate_check()
if duplicate_list == None:
    print("\nNo duplicates found !!!")
else:
    print(f"Duplicate_list {duplicate_list}")



