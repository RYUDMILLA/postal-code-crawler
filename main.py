from label import get_post
import csv

def initialize_csv(file):
    f = open(file, 'w+')
    writer = csv.writer(f)
    f.close()    
    
def save_to_file(dir_file, label):
  file = open(dir_file, mode = 'a', newline='')
  writer = csv.writer(file)
  writer.writerow([label])
  file.close()
  return

in_file = "label.csv"
out_file = "post.csv"
error_file = "error.csv"

initialize_csv(error_file)
initialize_csv(out_file)

in_csv = open(in_file, 'rt', encoding='UTF8')

done = 0
errored = 0
for label in in_csv:
    try:
        save_to_file(out_file, get_post(label))
        done += 1
        print(label, "Crawled")
    except AttributeError:
        save_to_file(out_file, ' ')
        save_to_file(error_file, label)
        errored += 1
        print(label, "Errored")

print(f"total : {done+errored} / done : {done} / errored : {errored}")
    