#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.


import csv


import csv

def writeNetworkScoresInCSV(filename, scores, networkID):
    # Write the header
    header = 'NET_neuronI_neuronJ'
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',', dialect="excel")
        writer.writerow([header, 'Strength'])

        # Write the scores
        for i in range(len(scores)):
            for j in range(len(scores[0])):
                v = scores[i][j]
                neuron_i_neuron_j_strength = networkID + '_' + str(i + 1) + '_' + str(j + 1)
                writer.writerow([neuron_i_neuron_j_strength, str(v)])

