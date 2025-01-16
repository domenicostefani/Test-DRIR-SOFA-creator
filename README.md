Test DRIR SOFA creator
---

The scripts in this repository use the `sofar` Python library to take a SOFA file for 6DoF Ambisonics rendering (Single source) and allows to modify the number of channels and length of the impulse responses.  
The output files are used for __computational load measurement__ of 6DoF plugins (in particular SPARTA 6DoFConv and the modified [6DoFMCFXConv](https://github.com/domenicostefani/SPARTA_Multi6DoF_project/tree/develop/) plugin).

__WARNING:__ The output sofas are not usable for anything else than computational load measurement, as they just cut channels and IRs, or inflate them with copies of other IRs and white noise at -30 dB.

Files:
- `0-update_DRIR_SOFA.py:` This is only useful with our old SOFA that you can find [here (www.angelofarina.it/Public/PHE-2020/6DOF/Tindari.sofa)](http://www.angelofarina.it/Public/PHE-2020/6DOF/Tindari.sofa).
- `1-drop_listenerPositions_from_tindari.py:` This script drops most of the listener positions from the updated Tindari SOFA to speed up loading during testing. Listener positions only affect ram usage but three are enough to stress the CPU with position change.
- `2-modify_SOFA.py`: This is the most important script. It takes a SOFA file and creates a new one with the desired number of channels and length of the impulse responses. Reducing either results in cutting, while increasing channels results in just copying some of the existing IRs, and increasing IR length results in adding white noise at -30 dB.
- `3-create_test_sofas.py`: This script calls `2-modify_SOFA.py` multiple times to create a set of SOFA files for the measurements for our paper.

_Domenico Stefani, Jan 2025_