"""
 @author Le Nhan Pham
 @website https://lenhanpham.github.io/
 @create date 2023-01-30 21:37:41
 @modify date 2023-01-30 21:37:41
"""


def extractTd(file):
    """
    This fucntion is used when tdddft 50-50 is used in the input of Gaussian
    """
    ss = 'Excitation energies and oscillator strengths'
    with open(file, 'r') as f:
        numSstates = 0
        numTstates = 0
        Senergies, Tenergies, Sstates, Tstates = [], [], [], []
        for line in f:
            if 'Excited State' in line:
                    tempState = line.split()[3].split('-')[0]
                    tempEnergy =float(line.split()[4])
                    if float(tempState) == 3.000:
                        Tenergies.append(tempEnergy)
                        numTstates += 1 
                        Tstates.append(numTstates)
                    elif float(tempState) ==  1.000:
                        Senergies.append(float(line.split()[4]))
                        numSstates += 1
                        Sstates.append(numSstates)

        singlets = dict(zip(Sstates, Senergies))
        triplets = dict(zip(Tstates, Tenergies))

        return singlets, triplets

def extractData2files(tdFile,):
    """
    This function is used when TDDFT runs for singlet and triplet are run separately
    """
    ss = 'Excitation energies and oscillator strengths'
    with open(tdFile, 'r') as f:
        numSstates = 0
        numTstates = 0
        Senergies, Sstates, Tenergies, Tstates = [], [], [], []
        for line in f:
            if 'Excited State' in line:
                    tempState = line.split()[3].split("-")[0]
                    tempEnergy =float(line.split()[4])
                    if str(tempState) == "Singlet":
                        Senergies.append(tempEnergy)
                        numSstates += 1 
                        Sstates.append(numSstates)
                    elif str(tempState) == "Triplet":
                        Tenergies.append(tempEnergy)
                        numTstates += 1
                        Tstates.append(numTstates)

        singlets = dict(zip(Sstates, Senergies))
        triplets = dict(zip(Tstates,Tenergies))
        if str(tempState) == "Singlet":
            return singlets
        else:
            return triplets