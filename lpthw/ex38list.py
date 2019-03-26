thing = '''       Based in Irvine, CA we are one of the leading real estate marketplace platforms 
on web and mobile in the US. We receive a trillion gigabytes of raw data a month and are in need of
talented Data Analysts to extract and transform the data into usable information. The ideal candidate
will have experience working with raw data and must be proficient with ETL, SSIS and SQL.           '''

fixed_thing_string = thing.strip()
#print(fixed_thing_string)

bucketlist = fixed_thing_string.split(' ')
#print(bucketlist)

list_a = []
for item in bucketlist:
    if item[0] == 'a' or item[0] == 'b':
        list_a += item.split(' ')
        sort_list = sorted(list_a)
        
print(sort_list)
print(len(sort_list))
while len(sort_list) < 3:
    print(sort_list)