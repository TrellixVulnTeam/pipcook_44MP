const Web3 = require('web3');
const Tx = require('ethereumjs-tx').Transaction; //交易事务
const rpcURL = 'https://kovan.infura.io/v3/732bed0994c14471a2d4793e035bf944';
const web3 = new Web3(rpcURL);

web3.eth.getGasPrice().then((result) => {
    console.log('wei' + result);
    console.log('ether:' + web3.utils.fromWei(result, 'ether'));
})