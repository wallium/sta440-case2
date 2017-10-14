import csv

buckets = [0, 0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 10, 15, 20, 25, 30]
predictors = ["male", "black", "hisp", "sn1", "sn2", "sn3"]

# Returns the period interval the time falls in (1-indexed)
def classify(time):
	for i in range(len(buckets)):
		if time < buckets[i]:
			return i
	# time is beyond any of the intervals
	return len(buckets)


def writePatient(filewriter, id, row):
	period = classify(float(row["nctdel"]))
	vals = []
	for pred in predictors:
		vals.append(row[pred])
	for i in range(period):
		periods = [0]*(len(buckets)-1)
		periods[i] = 1
		nextRow = [id]
		nextRow.append(1 if i == period-1 and row['fail'] == '1' else 0)
		nextRow.append(period)
		nextRow.extend(periods)
		nextRow.extend(vals)
		filewriter.writerow(nextRow)

with open('kellydat.txt') as csvfile, open('processed.csv', 'wb') as newcsv:
	reader = csv.DictReader(csvfile, delimiter=' ')
	filewriter = csv.writer(newcsv, delimiter=' ')
	header = ['id', 'assessment', 'period']
	for i in range(len(buckets)-1):
		header.append('p' + str(i+1))
	header.extend(predictors)
	filewriter.writerow(header)
	id = 1
	for row in reader:
		writePatient(filewriter, id, row)
		id = id + 1