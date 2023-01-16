# Convert 1/K0 Values to CCS Values

Script that uses Bruker's TDF-SDK 2.8.7.1 API to convert 1/K0 values to CCS values given an m/z value and ion charge are provided.

## Usage

1. Download this repo:
```
git clone https://github.com/gtluu/ook0_to_ccs
```
2. In the terminal (i.e. bash, Anaconda Prompt, etc.), navigate to the repo location:
```
cd /path/to/ook0_to_ccs
```
3. Run the script. The following example uses experimental data for Sclerotigenin:
```
python ook0_to_ccs.py --ook0 0.807 --charge 1 --mz 278.0885
```
4. The input and results will be printed:
```
1/K0: 0.807
Charge: 1
m/z: 278.0885
Calculated CCS Value: 169.54515038956174 Å
```