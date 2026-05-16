data_list = [{"roll_number": "100"}, {"name": "jack"}, {"subject": "science"},{"result" : "pass"}]

school_data = [(k,v) for item in data_list for k,v in item.items()]
print(school_data.items)