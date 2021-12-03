import sys
import seqlib

myfasta = seqlib.read_fasta(sys.argv[1])

maxgc = 0
seqname = ""
for name, seq in myfasta:
    gc = seqlib.gc(seq)
    if gc > maxgc:
        maxgc = gc
        seqname = name

maxgc = maxgc * 100

print(seqname)
print(f"{maxgc:f}")
