Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> import os
>>> os.chdir('C:\libsvm-3.22\python')
>>> import sys
>>> sys.path.append('C:\libsvm-3.22\python')
>>> from svmutil import *
>>> y,x=svm_read_problem('train.txt')
>>> yt,xt=svm_read_problem('test.txt')
>>> model=svm_train(y,x,['-t',1])
>>>  p_label, p_acc, p_val = svm_predict(yt, xt, model)
SyntaxError: unexpected indent
>>> p_label, p_acc, p_val = svm_predict(yt, xt, model)
Accuracy = 60.3717% (812/1345) (classification)
>>> 
