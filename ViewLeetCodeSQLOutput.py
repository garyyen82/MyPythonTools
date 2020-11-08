import re

# Get input from user
input=input('Copy and paste your LeetCode SQL result:')
  # sample input
  # input='{"headers": ["Id", "Client_Id", "Driver_Id", "City_Id", "Status", "Request_at", "Users_Id", "Banned", "Role", "Users_Id", "Banned", "Role"], "values": [[9, 3, 10, 12, "completed", "2013-10-03", 3, "No", "client", 10, "No", "driver"], [5, 1, 10, 1, "completed", "2013-10-02", 1, "No", "client", 10, "No", "driver"], [1, 1, 10, 1, "completed", "2013-10-01", 1, "No", "client", 10, "No", "driver"], [6, 2, 11, 6, "completed", "2013-10-02", 2, "Yes", "client", 11, "No", "driver"], [2, 2, 11, 1, "cancelled_by_driver", "2013-10-01", 2, "Yes", "client", 11, "No", "driver"], [8, 2, 12, 12, "completed", "2013-10-03", 2, "Yes", "client", 12, "No", "driver"], [7, 3, 12, 6, "completed", "2013-10-02", 3, "No", "client", 12, "No", "driver"], [3, 3, 12, 6, "completed", "2013-10-01", 3, "No", "client", 12, "No", "driver"], [10, 4, 13, 12, "cancelled_by_driver", "2013-10-03", 4, "No", "client", 13, "No", "driver"], [4, 4, 13, 6, "cancelled_by_client", "2013-10-01", 4, "No", "client", 13, "No", "driver"]]}'

# Split into list using regex
input=re.findall(r"[\w'-]+",input)
# Find headers and values lists
headersList=input[:input.index('values')]
valuesList=input[input.index('values'):]
# Contruct dictionary
d={}
# Get headers in dictionary
d[headersList.pop(0)]=headersList
numberOfHeaders=len(d['headers'])

# Get values in dictionary as list of lists
d[valuesList.pop(0)]=[[]]
d['values']=[valuesList[i:i+numberOfHeaders] for i in range(0,len(valuesList),numberOfHeaders)]

# Record the column size to reserve
columnSize=[0]*len(d['headers'])
for i,x in enumerate(d['headers']):
  columnSize[i]=len(x)+2

# Find out of column size adjustment needed based on values
for x in d['values']:
  for i,y in enumerate(x):
    if len(str(y))+2>columnSize[i]:
      columnSize[i]=len(y)+2

# This is the total size of the table
totalLength=sum(columnSize)+len(columnSize)+1

# Construct horizontal line
horizontalLine='+'
for x in columnSize:
  horizontalLine+='-'*x
  horizontalLine+='+'

# Initiate the table string starting with horizontal line
tableStr=horizontalLine+'\n'

# Add headers to table string
tableStr+='|'
for i,x in enumerate(d['headers']):
  tableStr+=" "+str(x)
  tableStr+=" "*(columnSize[i]-len(str(x))-1)
  tableStr+='|'
tableStr+='\n'

# Add another horizontal line beneath headers
tableStr+=horizontalLine+'\n'

# Add all the list of values under the headers
for x in d['values']:
  tableStr+='|'
  for i,y in enumerate(x):
    tableStr+=" "+str(y)
    tableStr+=" "*(columnSize[i]-len(str(y))-1)
    tableStr+='|'
  tableStr+='\n'

# Add another horizontal line to close the table
tableStr+=horizontalLine

print(tableStr)
