set "file_path=HW_Chaz.csv"

if exist "%file_path%" (
    del "%file_path%"
    echo File deleted.
) 

python VRun.py --test=Production_Heera --isModel=false --TestsDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --TestsCfgDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --PlaylistDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --bot_file="C:\Users\1000296249\Documents\HW_Training_Sequence\8D_BGA_DC\8D_HW_Characterisation\TM667.bot" --adapter="0" --enableSctpJumptorom=True

echo "Please power cycle the drive. After power cycling pressing any key."
pause

python VRun.py --test=HW_Training_Sequence

python VRun.py --test=Production_Heera --isModel=false --TestsDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --TestsCfgDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --PlaylistDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --bot_file="C:\Users\1000296249\Documents\HW_Training_Sequence\8D_BGA_DC\8D_HW_Characterisation\TM533.bot" --adapter="0" --enableSctpJumptorom=True

echo "Please power cycle the drive. After power cycling pressing any key."
pause

python VRun.py --test=HW_Training_Sequence

python VRun.py --test=Production_Heera --isModel=false --TestsDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --TestsCfgDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --PlaylistDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --bot_file="C:\Users\1000296249\Documents\HW_Training_Sequence\8D_BGA_DC\8D_HW_Characterisation\TM400.bot" --adapter="0" --enableSctpJumptorom=True

echo "Please power cycle the drive. After power cycling pressing any key."
pause

python VRun.py --test=HW_Training_Sequence

python VRun.py --test=Production_Heera --isModel=false --TestsDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --TestsCfgDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --PlaylistDir="C:\Program Files (x86)\SanDisk\CVF_2.0_x64\Python" --bot_file="C:\Users\1000296249\Documents\HW_Training_Sequence\8D_BGA_DC\8D_HW_Characterisation\TM200.bot" --adapter="0" --enableSctpJumptorom=True

echo "Please power cycle the drive. After power cycling pressing any key."
pause

python VRun.py --test=HW_Training_Sequence

python finalData.py