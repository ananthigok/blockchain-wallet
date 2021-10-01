# Multi-Blockchain Wallet in Python
In this assignment, Bitcoin Testnet Transactions and Local PoA Ethereum transactions were done which involved linking the transaction signing libraries - bit and web3.py - the coding part is done in wallet.py
<kbd>![Blockchain Wallet](Screenshots/newtons-coin-cradle.jpeg)

The following dependencies are required for this assignment and the project set up with insatllation guidelines are expalined in the requirements.txt file:
 - HD Wallet Derive Installation
 
 <kbd>![Command](Screenshots/hd-wallet-derive-cmd-line.png)
  
- Derived the wallet keys
  
<kbd>![Command](Screenshots/hd-wallet-derive.png)

 - Blockchain TX Installation

 ## Short description of the Wallet
 
- A Mnemonic was created using [the online tool](https://iancoleman.io/bip39/) initially 
 
- A php derive command is created with the Mnemonic, the coin type, also adding the numderive depth in the command defines the number of children accounts to retain from data 
<kbd>![Command](Screenshots/command.png)
 
- The output data is retrieved by running the above command 
 <kbd>![Derive](Screenshots/derive-output.png)
  
- With the privkey from the data retained and using method "priv_key_to_account" the sender Account and recipient address is fetched
- By passing the account, amount and coin details to create and send transaction functions - the transaction is done 
 <kbd>![Command](Screenshots/code-def-transactions.png) 

Bitcoin transaction was done using this [testnet faucet](https://testnet-faucet.mempool.co/).
<kbd>![Bitcoin Transaction](Screenshots/bitcoin-testnet-transaction.png)
 
<kbd>![Wallet](Screenshots/transaction-faucet.png)
 
##Local PoA Ethereum transaction
<kbd>![Transaction-Success](Screenshots/Transaction-success-wallet.png)
<kbd>![Transaction](Screenshots/transaction-wallet.png)
