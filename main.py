import math

waveform = {
    "15": [
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333],
        [1, 0.0333],
        [0, 0.0333] 
    ]
}
phase = 3
buff_size = 2048
out_buff = []

def init():
    global out_buff
    global buff_size
    buff_size = int(buff_size)
    if math.pow(2, math.floor(math.log2(buff_size))) != buff_size:
        raise ValueError("buff_size is not a power of 2.")
    out_buff = [[0] * buff_size] * phase
    for wave_key in waveform.keys():
        for i in range(1, len(waveform[wave_key])):
            waveform[wave_key][i][1] += waveform[wave_key][i - 1][1]
    print(waveform)

def main():
    init()

main()