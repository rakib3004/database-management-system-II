
from email.message import Message
from fileinput import filename
from os import system
import re
import tkinter as tk
from tkinter import CENTER, RAISED, StringVar, filedialog
from turtle import st
import itertools

def browseFiles():
    global fileName
    fileName = filedialog.askopenfilename(  initialdir = "/",
                                            title = "Select a Dataset",
                                            filetypes = (("Text files", "*.csv*"),("all files", "*.*")))
    explore_var.set(fileName)

def submit():
    global minSup, minCon,  dataSetFileName
    if support_var.get()!='' : minimumSupport = float(support_var.get())
    if confidence_var.get()!='' : minimumConfidence = float(confidence_var.get())
    dataSetFileName = fileName
    root.destroy()



def generateC1(dataSet):
    productDict = {}
    returneSet = []
    for data in dataSet:
        for product in data:
            if product not in productDict:
               productDict[product] = 1
            else:
                 productDict[product] = productDict[product] + 1
    for key in productDict:
        tempArray = []
        tempArray.append(key)
        returneSet.append(tempArray)
        returneSet.append(productDict[key])
        tempArray = []
    return returneSet


def generateFrequentItemSet(CandidateList, noOfTransactions, minimumSupport, dataSet, fatherFrequentArray):
    frequentItemsArray = []
    for i in range(len(CandidateList)):
        if i%2 != 0:
            support = (CandidateList[i] * 1.0 / noOfTransactions) * 100
            if support >= minimumSupport:
                frequentItemsArray.append(CandidateList[i-1])
                frequentItemsArray.append(CandidateList[i])
            else:
                eleminatedItemsArray.append(CandidateList[i-1])

    for k in frequentItemsArray:
        fatherFrequentArray.append(k)

    if len(frequentItemsArray) == 2 or len(frequentItemsArray) == 0:
        #print("This will be returned")
        returnArray = fatherFrequentArray
        return returnArray

    else:
        generateCandidateSets(dataSet, eleminatedItemsArray, frequentItemsArray, noOfTransactions, minimumSupport)


def generateCandidateSets(dataSet, eleminatedItemsArray, frequentItemsArray, noOfTransactions, minimumSupport):
    onlyElements = []
    arrayAfterCombinations = []
    candidateSetArray = []
    for i in range(len(frequentItemsArray)):
        if i%2 == 0:
            onlyElements.append(frequentItemsArray[i])
    for item in onlyElements:
        tempCombinationArray = []
        k = onlyElements.index(item)
        for i in range(k + 1, len(onlyElements)):
            for j in item:
                if j not in tempCombinationArray:
                    tempCombinationArray.append(j)
            for m in onlyElements[i]:
                if m not in tempCombinationArray:
                    tempCombinationArray.append(m)
            arrayAfterCombinations.append(tempCombinationArray)
            tempCombinationArray = []
    sortedCombinationArray = []
    uniqueCombinationArray = []
    for i in arrayAfterCombinations:
        sortedCombinationArray.append(sorted(i))
    for i in sortedCombinationArray:
        if i not in uniqueCombinationArray:
            uniqueCombinationArray.append(i)
    arrayAfterCombinations = uniqueCombinationArray
    for item in arrayAfterCombinations:
        count = 0
        for transaction in dataSet:
            if set(item).issubset(set(transaction)):
                count = count + 1
        if count != 0:
            candidateSetArray.append(item)
            candidateSetArray.append(count)
    generateFrequentItemSet(candidateSetArray, noOfTransactions, minimumSupport, dataSet, fatherFrequentArray)

def generateAssociationRule(freqSet):
    associationRule = []
    for item in freqSet:
        if isinstance(item, list):
            if len(item) != 0:
                length = len(item) - 1
                while length > 0:
                    combinations = list(itertools.combinations(item, length))
                    temp = []
                    LHS = []
                    for RHS in combinations:
                        LHS = set(item) - set(RHS)
                        temp.append(list(LHS))
                        temp.append(list(RHS))
                        #print(temp)
                        associationRule.append(temp)
                        temp = []
                    length = length - 1
    return associationRule

def aprioriOutput(rules, dataSet, minimumSupport, minimumConfidence):
    returnAprioriOutput = []
    for rule in rules:
        supportOfX = 0
        supportOfXinPercentage = 0
        supportOfXandY = 0
        supportOfXandYinPercentage = 0
        for transaction in dataSet:
            if set(rule[0]).issubset(set(transaction)):
                supportOfX = supportOfX + 1
            if set(rule[0] + rule[1]).issubset(set(transaction)):
                supportOfXandY = supportOfXandY + 1
        supportOfXinPercentage = (supportOfX * 1.0 / noOfTransactions) * 100
        supportOfXandYinPercentage = (supportOfXandY * 1.0 / noOfTransactions) * 100
        confidence = (supportOfXandYinPercentage / supportOfXinPercentage) * 100
        if confidence >= minimumConfidence:
            supportOfXAppendString = "Support Of X: " + str(round(supportOfXinPercentage, 2))
            supportOfXandYAppendString = "Support of X & Y: " + str(round(supportOfXandYinPercentage))
            confidenceAppendString = "Confidence: " + str(round(confidence))

            returnAprioriOutput.append(supportOfXAppendString)
            returnAprioriOutput.append(supportOfXandYAppendString)
            returnAprioriOutput.append(confidenceAppendString)
            returnAprioriOutput.append(rule)

    return returnAprioriOutput



root = tk.Tk()
root.geometry("1000x1000")
root.title("Apriori Algorithm")

minSup = 20
minCon = 50
dataset = ''
fileName = 'data\\transaction.csv'

support_var = tk.StringVar()
confidence_var = tk.StringVar()
explore_var = tk.StringVar()

explore_label = tk.Label(root, text='Dataset', font=('bold'))
explore_entry = tk.Entry(root, textvariable=explore_var, font=('bold'))
button_explore = tk.Button(root, text="Select", command=browseFiles)

support_label = tk.Label(root, text='Minimum Support', font=('bold'))
support_entry = tk.Entry(root, textvariable=support_var, font=('bold'))

confidence_label = tk.Label(root, text='Minimum Confidence', font=('bold'))
confidence_entry = tk.Entry(root, textvariable=confidence_var, font=('bold'))


sub_btn = tk.Button(root, text='Submit', font=('normal'), command=submit, bg="red")


explore_label.place(x=350, y=300)
explore_entry.place(x=500, y=300)
button_explore.place(x=700, y=300)

support_label.place(x=350, y=340)
support_entry.place(x=500, y=340)

confidence_label.place(x=350, y=380)
confidence_entry.place(x=500, y=380)


sub_btn.place(x=500, y=500, anchor=CENTER)

root.mainloop()





res = tk.Tk()
res.title("@Author: Md. Rakib Trofder")
res.geometry("1000x1300")

msg = 'Apriori Algorithm'
title_label = tk.Label(res, text=msg, font=("Arial", 20, "bold"))
title_label.place(x=350, y=0)




msg = '@Author: Md. Rakib Trofder'


minimumSupport=20
minimumConfidence = 30

nonFrequentSets = []
allFrequentItemSets = []
tempFrequentItemSets = []
dataSet = []
eleminatedItemsArray = []
noOfTransactions = 0
fatherFrequentArray = []
something = 0


#   Reading the data file line by line
with open(dataSetFileName,'r') as fp:
    lines = fp.readlines()

for line in lines:
    line = line.rstrip()
    dataSet.append(line.split(","))

noOfTransactions = len(dataSet)

firstCandidateSet = generateC1(dataSet)

frequentItemSet = generateFrequentItemSet(firstCandidateSet, noOfTransactions, minimumSupport, dataSet, fatherFrequentArray)

associationRules = generateAssociationRule(fatherFrequentArray)

AprioriOutput = aprioriOutput(associationRules, dataSet, minimumSupport, minimumConfidence)

outcome=""
counter = 0
if len(AprioriOutput) == 0:
    outcome=" "
else:
    for i in AprioriOutput:
        #outcome=outcome+str(i)
        if counter == 3:
            print(str(i) + "------>" + str(i))
            outcome=outcome+"   "+str(i) + "------>" + str(i)+"\n"
            #print(outcome+'!!!!!!!!!')
            counter = 0
        else:
            #print(i, end='  ')
            outcome = outcome+"   "+str(i) + "   "
            counter = counter + 1

msg =''

par_label = tk.Label(res, text=msg)




msg = outcome

#freq_lebel = tk.Label(res, text=msg)

msg = ' '


rule_label = tk.Label(res, text=msg)



text_widget = tk.Text(res, height=45, width=180)

scroll_bar = tk.Scrollbar(res)


scroll_bar.pack(side=tk.RIGHT)


text_widget.pack(side=tk.LEFT)

long_text = outcome

text_widget.insert(tk.END, long_text)
text_widget.place(x=0, y=32)


#freq_lebel.place(x=25, y=60)
res.mainloop()