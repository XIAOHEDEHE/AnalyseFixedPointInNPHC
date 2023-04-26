# README
This folder will process the output of the NPHC, and the interpretation of the files are below:

- 'detec_positive.py'
  - file 'detec_positive.py' has three functions for now: 'print_reslut','returen_result','return_real'. 
  - 'print_result' and 'return_result' are similar, they will withdraw the number of the positive real solution from the output of NPHC. The only difference between them is 'print_result' will print the result, and 'return_result' will only return the value without printing.
  - 'return_real' will return the number of the real solution.
- 'withdraw_positive_real.py'
  - This file is gonna to withdraw the number of the positive real solution and save the matrix to the file 'positive_real.txt'. It's convenient if you want to visualize the result.
- 'withdraw_real.py'
  - Withdraw the number of the real solution and save the the matrix to the file 'real.txt'
- 'withdraw_real_value.py'
  - Withdraw the value of the real positive solution and save the matrix to the folder 'output_real'
- 'main.py'
  - Main funtion.
- 'mse.py'
  - Calculate the MSE(Mean squared error).