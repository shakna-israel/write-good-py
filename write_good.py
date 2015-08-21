import argparse

def get_cli_flags():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="The input file. Hopefully plain text.")
    parser.add_argument("-o", "--output", help="An output file to generate.")
    cliArgs = parser.parse_args()
    if cliArgs.input:
        inFile = cliArgs.input
    else:
        inFile = False
    if cliArgs.output:
        outFile = cliArgs.output
    else:
        outFile = cliArgs.output
    return { "inFile": inFile, "outFile": outFile }

def check_passive(lineInFile, countInFile):
    regular_passives = ["am","are","were","being","is","been","was","be"]
    irregular_passives = ['awoken','been','born','beat','become','begun','bent','beset','bet','bid','bidden','bound','bitten','bled','blown','broken','bred','brought','broadcast','built','burnt','burst','bought','cast','caught','chosen','clung','come','cost','crept','cut','dealt','dug','dived','done','drawn','dreamt','driven','drunk','eaten','fallen','fed','felt','fought','found','fit','fled','flung','flown','forbidden','forgotten','foregone','forgiven','forsaken','frozen','gotten','given','gone','ground','grown','hung','heard','hidden','hit','held','hurt','kept','knelt','knit','known','laid','led','leapt','learnt','left','lent','let','lain','lighted','lost','made','meant','met','misspelt','mistaken','mown','overcome','overdone','overtaken','overthrown','paid','pled','proven','put','quit','read','rid','ridden','rung','risen','run','sawn','said','seen','sought','sold','sent','set','sewn','shaken','shaven','shorn','shed','shone','shod','shot','shown','shrunk','shut','sung','sunk','sat','slept','slain','slid','slung','slit','smitten','sown','spoken','sped','spent','spilt','spun','spit','split','spread','sprung','stood','stolen','stuck','stung','stunk','stridden','struck','strung','striven','sworn','swept','swollen','swum','swung','taken','taught','torn','told','thought','thrived','thrown','thrust','trodden','understood','upheld','upset','woken','worn','woven','wed','wept','wound','won','withheld','withstood','wrung','written']
    check_phrases = [" \'", ' \"', "\', ", '\",']
    for checkItem in check_phrases:
        if checkItem in lineInFile.lower():
            for regItem in regular_passives:
                if regItem in lineInFile.lower():
                    print("Line " + str(countInFile) + ", contains passive voice.")
            for irregItem in irregular_passives:
                if irregItem in lineInFile.lower():
                    print("Line " + str(countInFile) + ", may contain passive voice.")

def check_illusion(lineInFile, countInFile):
    prevword = ""
    for word in lineInFile.split():
        if word.lower() == prevword.lower():
            print("Line " + str(countInFile) + ", contains double words.")
        prevword = word

def check_so(lineInFile, countInFile):
    wordList = lineInFile.split()
    if wordList[0].lower() == "so":
        print("Line " + str(countInFile) + ", starts with the word 'So'.")

def check_thereIs(lineInFile, countInFile):
    wordList = lineInFile.split()
    if wordList[0].lower() == "there":
        if wordList[1].lower() == "is":
            print("Line " + str(countInFile) + ", starts with 'There is'.")
        if wordList[1].lower() == "are":
            print("Line " + str(countInFile) + ", starts with 'There are'.")

def check_weasel(lineInFile, countInFile):
    weasel_words = ["a lot","about","acts","again","all","almost","already","also","anyway","appeared","appears","are a number","arguably","back","be able to","began","believed","better","bit","clearly","close","combats","completely","considered","could","decided","down","effective","efficient","enough","even","ever","exceedingly","excellent","expert","experts","extremely","fairly","far","felt","few","gains","heard","helps","huge","improved","interestingly","is a number","is like","just","knew","largely","like","linked to","literally","looked","looks","lots","many","might","most","mostly","not rocket science","noticed","often","only","outside the box","over","own","pretty","probably","quite","rather","real","realised","realized","really","recognised","recognized","relatively","remarkably","reportedly","saw","seemed","seems","several","significantly","smelled","so","some","somehow","sort","started","still","substantially","supports","supposed","surprisingly","that","then","thought","tiny","touched","understood","up","useful","various","vast","very","virtually","wanted","watched","well","wished","wondered","works"]
    check_phrases = [" \'", ' \"', "\', ", '\",']
    for checkItem in check_phrases:
        if checkItem in lineInFile.lower():
            for weasel in weasel_words:
                if weasel in lineInFile.lower():
                    print("Line " + str(countInFile) + ", contains a weasel word: " + str(weasel) + ".")

def check_adverb(lineInFile, countInFile):
    print("")

def check_tooWordy(lineInFile, countInFile):
    print("")

def check_cliches(lineInFile, countInFile):
    print("")

def main():
    inFile = get_cli_flags()['inFile']
    if inFile == False:
        raise OSError
    outFile = get_cli_flags()['outFile']
    with open(inFile, 'r') as inputFile:
        lineCounter = 0
        for line in inputFile:
            lineCounter = int(lineCounter) + 1
            check_passive(line, lineCounter)
            check_illusion(line, lineCounter)
            check_so(line, lineCounter)
            check_thereIs(line, lineCounter)
            check_weasel(line, lineCounter)
           # check_adverb(line, lineCounter)
           # check_tooWordy(line, lineCounter)
           # check_cliches(line, lineCounter)

if __name__ == "__main__":
    main()
