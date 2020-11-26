const Web3 = require('web3');
const Tx = require('ethereumjs-tx').Transaction; //交易事务
const rpcURL = 'https://kovan.infura.io/v3/732bed0994c14471a2d4793e035bf944';
const web3 = new Web3(rpcURL);

web3.eth.getBlockNumber().then(console.log); //22164001 区块数
web3.eth.getBlock('latest').then(console.log);