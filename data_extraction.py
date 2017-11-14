from conllu.parser import parse, parse_tree

with open('en-ud-dev.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

# print(data)

# data = """
# 1   The the DET DT  Definite=Def|PronType=Art   4   det _   _
# 2   quick   quick   ADJ JJ  Degree=Pos  4   amod    _   _
# 3   brown   brown   ADJ JJ  Degree=Pos  4   amod    _   _
# 4   fox fox NOUN    NN  Number=Sing 5   nsubj   _   _
# 5   jumps   jump    VERB    VBZ Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   0   root    _   _
# 6   over    over    ADP IN  _   9   case    _   _
# 7   the the DET DT  Definite=Def|PronType=Art   9   det _   _
# 8   lazy    lazy    ADJ JJ  Degree=Pos  9   amod    _   _
# 9   dog dog NOUN    NN  Number=Sing 5   nmod    _   SpaceAfter=No
# 10  .   .   PUNCT   .   _   5   punct   _   _
#
# """

# import re
# data = re.sub(r" +", r"\t", data)

results = parse(data)
print("results =")
print(results)
