# toby-ben is a crypto trading bot for the Coinbase Pro API 

## Basic Structure
It uses peewee/python2 to save data to a local mysql db at regular intervals, and uses that data to make trading decisions.  
It is designed to easily allow for the implementation of new bidding strategies, which are separated into **when to bid** and **how much to bid** classes.

## Future Work
The bot functions locally and has made plenty of smart trades, but it's also made some dumb ones :) 
Next steps would be to host it on AWS, implement more robust bidding logic, and pull crypto data from a 3rd party API instead of maintaining it locally.  



