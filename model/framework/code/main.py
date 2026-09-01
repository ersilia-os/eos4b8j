from bs4 import BeautifulSoup
import requests
import urllib
import sys
import csv

# Input Parameters

input_file = open(sys.argv[1], 'r')
Lines = input_file.readlines()[1:]
fp     = 'ECfp4'
db     = 'GDBChEMBL'
nnc    = '100'


data = []
for input_smiles in Lines:
    input_smiles = input_smiles.strip() 
    url_encoded_smiles = urllib.parse.quote(input_smiles)

    url = 'https://gdb-chembl-simsearch.gdb.tools/search?smi=' + url_encoded_smiles +  '&fp=' + fp + '&db=' + db + '&nnc=' + nnc
    r = requests.get(url, timeout = 60)

    if r.status_code != 200:
        data += [[[], []]]
        continue

    soup = BeautifulSoup(r.text, features = 'html.parser')
    results = soup.find_all('script')
    if not results:
        data += [[[], []]]
        continue
    T = str(results[-1]).splitlines()
    T = [i for i in T if not ('IDX' not in i)]
    smiles_list = []
    similarity_indices = []
    for i in T:
        x = i.split('+\"')
        x1 = x[1].split("IDX")
        x2 = x1[0]
        smiles_list.append(x2.strip(' ')) 
        similarity_indices.append(float(x[3].strip('\"')))
    paired = list(zip(smiles_list, similarity_indices))
    paired.sort(key=lambda x: (-x[1], x[0]))
    sorted_smiles_list = [smi for smi, _ in paired]
    sorted_similarity_indices = [sim for _, sim in paired]
    data += [[sorted_smiles_list, sorted_similarity_indices]]


n_cols = int(nnc)
header = [f"smi_{i:02}" for i in range(n_cols)]
with open(sys.argv[2], "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for d in data:
        row = d[0][:n_cols]
        writer.writerow(row + [""] * (n_cols - len(row)))
