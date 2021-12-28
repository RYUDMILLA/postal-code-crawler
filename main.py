from label import get_post
import csv

def initialize_csv(file):
    f = open(file, 'w+')
    writer = csv.writer(f)
    f.close()    
    
def save_to_file(dir_file, center):
  file = open(dir_file, mode = 'a', newline='')
  writer = csv.writer(file)
  writer.writerow([center])
  file.close()
  return

out_file = "post_final.csv"
error_file = "error_final.csv"
in_file = "label.csv"

initialize_csv(error_file)
initialize_csv(out_file)

in_csv = open(in_file, 'rt', encoding='UTF8')

done = 0
errored = 0
for center in in_csv:
    center = center.strip().strip('\"')
    try:
        save_to_file(out_file, get_post(center))
        done += 1
        print(done, "Crawled")
    except AttributeError:
        save_to_file(out_file, ' ')
        save_to_file(error_file, center.strip('\"'))
        errored += 1
        print(errored, "Errored")
    
    