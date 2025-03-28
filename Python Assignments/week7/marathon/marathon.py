def main():
    results = readFile('marathon.txt')
    option = ''
    while option != 'Q':
        menu()
        option = input('Select option: ')
        if option == 'S':
            displayCompetitor(results)
        elif option == 'I':
            displayNbrInInterval(results)

def readFile(filename):
    results = []
    file = open(filename)
    for line in file:
        result = {}  
        result['id'] = line.split(',')[0]
        result['time'] = line.split(',')[1]
        result['firstname'] = line.split(',')[2]
        result['lastname'] = line.split(',')[3]
        results.append(result)
    
    return results


def getIntervalData(shortest, longest, results):
    data = {'count':0,'mean':0}
    totaltime = 0
    for result in results:
        time = getSecs(result['time'])
        if time > shortest and time < longest:
            data['count'] += 1
            totaltime += time 
    data['mean'] = totaltime / data['count']   

    return data

def displayCompetitor(results):
    idNo = input('Enter competitor ID:')
    found = False
    for competitor in results:
        if competitor['id'] == idNo:
            displayCompetitorInfo(competitor)
            found = True
    if not found:
        print('Competitor not found')
    

def displayCompetitorInfo(competitor):
    print('ID :',competitor['id'])
    print('First Name :', competitor['firstname'])
    print('First Name :', competitor['lastname'])


def displayNbrInInterval(results):
    startTime = input('Enter start time of interval (hh:mm:ss): ')
    startSecs = getSecs(startTime)
    endTime = input('Enter end time of interval (hh:mm:ss): ')
    endSecs = getSecs(endTime)
    intervalData = getIntervalData(startSecs, endSecs, results)
    print('Number of competitors finishing in this interval = ', intervalData['count'])
    if intervalData['count'] != 0:
        secs = intervalData['mean']
        mins = secs//60
        secs = secs%60
        hours = mins//60
        mins = mins%60
        print('Mean time in interval is ',int(hours),'hours',int(mins),'minutes','and ',int(secs),'seconds')
    else:
        print('No competitors in interval')


def getSecs(time):
    timeSplit = time.split(':')
    seconds = int(timeSplit[2]) + 60*int(timeSplit[1]) + 60*60*int(timeSplit[0])
    return seconds


def menu():
    print('Options are:')
    print('S - Show data for a competitor')
    print('I - Show statistics for competitors finishing in a given interval')
    print('Q - Quit the program')


if __name__ == "__main__":
  main()