import os
import matplotlib.pyplot as plt

channel_numbers = [16,36,64]
ir_lengths_seconds = [0.1,0.2,0.5,1,2,5,10]
SAMPLE_RATE = 48000
SOFAFILE = './tindari_drop.sofa'



command = lambda id,ch, length_samp, lengthstring: f"python .\modify_SOFA.py -i {SOFAFILE} -o ./{id}_{ch}ch_{lengthstring}_tindari_drop.sofa -ch {ch} -l {length_samp}"


id = 0
test_x = []
test_y = []
test_label = []
for idch,ch in enumerate(channel_numbers):
    for length in ir_lengths_seconds:
        length_samp = int(length*SAMPLE_RATE)

        if length<1:
            lengthstring = f"{int(length*1000)}ms"
        else:
            lengthstring = f"{length}s"

        strid = str(id).zfill(3)
        print(command(strid,ch,length_samp,lengthstring))

        test_x.append(length + idch*(0.1*length))
        test_y.append(ch+length)
        test_label.append(f"{ch}ch {lengthstring}")
        
        id+=1


fig, ax = plt.subplots()

# Barplot with all different colors per bar
ax.bar(test_x, test_y, color=[f'C{i}' for i in range(len(test_x))])
# ax.set_xscale('log') 

ax.set_xticks(test_x)
ax.set_xticklabels(test_label, rotation=90)

plt.show()


