*** Settings ***
Library    ValuePair.py    ${4}    ${2}
Library    func.py

*** Test Cases ***    
ValuePair: Sum
    ${value}     SUM   
    Should Be Equal    ${value}    ${6}
ValuePair: Diff
    ${value}     DIFF   
    Should Be Equal    ${value}    ${2}

Func: Factorial
    ${value}    func.Factorial    ${3}
    Should Be Equal    ${value}    ${6}