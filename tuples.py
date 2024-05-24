def get_coordinate(record):
    return record[1]
def convert_coordinate(coordinate):
    a=coordinate[0]
    b=coordinate[1]
    return a,b
def create_record(azara_record, rui_record):
    a0=azara_record[0]
    a1=azara_record[1]
    r0=rui_record[0]
    r1=rui_record[1]
    r2=rui_record[2]
    a10=a1[0]
    a11=a1[1]
    a1depac=a10,a11
    if r1 == a1depac:
        return a0,a1,r0,r1,r2
    else:
        return "not a match"
