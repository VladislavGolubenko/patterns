class JsonData:
    def __init__(self, some_data):
        self.data = '{' + some_data + '}'

    def show_json(self):
        print(self.data)


class XMLData:
    def __init__(self, some_data):
        self.data = '<tag>' + some_data + '</tag>'

    def show_xml(self):
        print(self.data)


class Adapter(JsonData):

    def __init__(self, data):
        super(JsonData, self).__init__()
        self.data = data

    def convert_to_json(self):
        self.data = self.data.replace('<tag>', '{')
        self.data = self.data.replace('</tag>', '}')

        return self.show_json()


if __name__ == "__main__":

    string = 'Some data which I use to show'
    my_xml = XMLData(string)
    my_xml.show_xml()
    convertator = Adapter(my_xml.data)
    convertator.convert_to_json()

