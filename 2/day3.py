f = open(r'2/reports.txt', 'r')
reports = f.read()

report_list = reports.splitlines()

processed_reports = []

danger_count = 0

for report in report_list:
    report_processed = report.split()
    processed_reports.append(report_processed)

def danger_checker(report):
    danger = False
    increasing = False
    decreasing = False
    for i in range(0, len(report)-1):
        danger_check = abs(int(report[i]) - int(report[i+1]))
        if danger_check > 3:
            danger = True
        danger_check2 = int(report[i]) - int(report[i+1])
        if danger_check2 < 0:
            increasing = True
        elif danger_check2 > 0:
            decreasing = True
        elif danger_check2 == 0:
            danger = True
    
    if increasing and decreasing:
        danger = True
    
    return danger
    

print(len(processed_reports))
for report in processed_reports:
    danger = danger_checker(report)

    if not danger:
        danger_count += 1

print(danger_count)
    