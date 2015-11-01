#clean training data from unkown labels
import os, sys
f1 = open("output_clean_training.txt", "a")
sentence = []
train_sentence = []

doc = []
old_arr = ['', '']
remove=False
sentence_end = 0
idx = 0
sentence_count = 0
with open (sys.argv[1], "r") as f:
    for line in f:
        arr = line.split('\t')
        doc.append("\t".join(arr))

        if(arr[1] == 'LABEL\n'):
            remove = True

        if(arr[0]=='.' or arr[0]=='?' or arr[0]=='?'):
            sentence_start = sentence_end
            sentence_end = idx
            sentence_count +=1
            if(remove == True):
                remove=False
                del doc[sentence_start+1:sentence_end+1]
                diff = sentence_end - sentence_start
                sentence_end = sentence_end - diff
                sentence_start = sentence_start - diff
                idx = idx - diff
            else:
                remove=False


        idx+=1

f1.write("".join(doc))
f1.close()